#"Page 별 MD 출력"

# "section_info.json"
# Field 
# section_ID : ex 1, or 1.1 or 1.1.1 
# section_title : section title string 
# section_generation_order : 1, 2, 3, ... 
# section depth : 1, 2, 3, ...  (id 가 1 이면 1, 1.1 이면 2, 1.1.1 이면 3)
# type : toc or body
# page_start : page number where section starts(png page number)
# page_end : page number where section ends
# section_summary : section summary(section 내용이 짧으면 원본을 그대로 인용)
# section_content : section content(section 원본 md)
# section_image_name_list : section embeded image name
# section_image : endcoded image list
# section_table_list : section table name list
# section_table : markdown table list(same name should merged)


import os
import requests
import time
import re
from pdf2image import convert_from_path
import base64
import json
from pathlib import Path
from PIL import Image
import io
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

os.environ['PYTORCH_ALLOC_CONF'] = 'expandable_segments:True'

# --- 설정 ---
OLLAMA_BASE_URL = "http://localhost:11434"
MODEL_NAME = "qwen3-vl:32b-instruct-q4_K_M"
PDF_PATH = "./source_doc/NVM-Express-Base-Specification-Revision-2p3.pdf"
OUTPUT_PNG_FOLDER = "./out/output_png"
OUTPUT_JSON_FOLDER = "./out/output_json"
OUTPUT_MD_FOLDER = "./out/md"
RESULT_TXT_FILE = "./out/output_summary.txt"
# Configuration
TARGET_SECTION_ID = "5.2.12.1.19"
PDF_STRUCTURE_PATH = "./out/pdf_structure.json"

os.makedirs(OUTPUT_PNG_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_JSON_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_MD_FOLDER, exist_ok=True)

# Global State for Section Processing
sections = []
current_section = None
section_counter = 0
current_table_rows = []

IMPROVED_PROMPT = """
You are a NVMe specification document parser. Extract structured information from this page image.

**Instructions:**
1. **Strictly extract text visible in the document.** Do NOT generate, hallucinate, or add any text that is not present in the image.
2. Extract text with markdown formatting:
   - Identify section headings (e.g., '1. Introduction', '1.1 Overview') and format them as Markdown headers (#, ##, ###).
   - Do NOT format the document title or running headers as markdown headers.
   - Do NOT format Figure captions or Table titles as markdown headers (do not use #, ##, ### for them).
   - Do NOT output page metadata header (e.g., `===== page_number=...`).
3. **Image Extraction (CRITICAL):**
   - For EVERY figure or image, you MUST output a metadata comment line BEFORE the caption or image location.
   - Format: `<!-- Figure [Name], coordinate:(x1,y1,x2,y2) -->`
   - Example: `<!-- Figure 1, coordinate:(100,200,900,800) -->`
   - If the image has no name, use: `<!-- Embeded_Image [Index], coordinate:(x1,y1,x2,y2) -->`
   - *Coordinates must be normalized (0-1000).*
4. If parsing fails completely, output "extraction_error".
"""


def pdf_to_png(pdf_path, output_folder):
    """PDF를 PNG 이미지로 변환"""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF 파일을 찾을 수 없습니다: {pdf_path}")
    
    os.makedirs(output_folder, exist_ok=True)
    logger.info(f"🔄 PDF 변환 중: {pdf_path}")
    
    images = convert_from_path(pdf_path, dpi=200)
    png_files = []
    
    for i, img in enumerate(images):
        filename = os.path.join(output_folder, f"{i+1:04d}_page.png")
        img.save(filename, "PNG")
        png_files.append(filename)
    
    logger.info(f"✅ {len(images)}장의 PNG 이미지 생성 완료 → {output_folder}")
    return png_files


def encode_image_to_base64(image_path):
    """이미지를 base64로 인코딩"""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def crop_and_encode_image(image_path, coords):
    """
    Crop image based on coordinates (x1, y1, x2, y2) and return base64 string.
    Coordinates are assumed to be normalized (0-1000).
    """
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            
            # Normalize coordinates (0-1000 chars) to pixel values
            # Coords: (x1, y1, x2, y2)
            x1 = int(coords[0] * width / 1000)
            y1 = int(coords[1] * height / 1000)
            x2 = int(coords[2] * width / 1000)
            y2 = int(coords[3] * height / 1000)
            
            # Ensure valid box
            if x1 >= x2 or y1 >= y2:
                logger.warning(f"⚠️ Invalid coordinates for crop: {coords}")
                return None

            cropped_img = img.crop((x1, y1, x2, y2))
            
            # Convert to base64
            buffered = io.BytesIO()
            cropped_img.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
            return img_str
    except Exception as e:
        logger.error(f"❌ Image crop failed: {e}")
        return None

def call_ollama_vision(image_base64, prompt):
    """Ollama Vision API 호출 (단일 이미지)"""
    url = f"{OLLAMA_BASE_URL.rstrip('/')}/api/generate"
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "images": [image_base64],
        "options": {
            "temperature": 0.1,
            "num_ctx": 32768
        }
    }
    
    try:
        response = requests.post(url, json=payload, timeout=900)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "")
    except Exception as e:
        logger.error(f"❌ LLM 호출 실패: {e}")
        return "extraction_error"


def generate_summary_if_needed(text, section_title="", section_id=""):
    """Generate summary if text is too long, otherwise return text."""
    # If text is short, return as is.
    if len(text) < 500:
        return text
    
    # improved context for summary
    context_str = ""
    if section_id or section_title:
        context_str = f"Section: {section_id} {section_title}\n"
    
    prompt = f"""
You are an expert NVMe specification engineer.
{context_str}
Summarize the following section content in 3-5 concise sentences.
Focus on the main technical purpose, requirements, data structures, and key field definitions.
Avoid generic phrases. Capture specific constraints and behavioral definitions.

Content:
{text[:10000]}
"""
    
    url = f"{OLLAMA_BASE_URL.rstrip('/')}/api/generate"
    payload = {
        "model": MODEL_NAME, 
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.1,
            "num_ctx": 32768
        }
    }
    try:
        response = requests.post(url, json=payload, timeout=300)
        if response.status_code == 200:
            return response.json().get("response", "").strip()
    except Exception as e:
        logger.warning(f"⚠️ Summary generation failed: {e}")
    
    return text[:500] + "..." # Fallback


def parse_sections(page_md, page_num, section_map, png_path=None):
    """Parse sections from markdown content and update global sections list."""
    global current_section, section_counter, sections, current_table_rows

    lines = page_md.split('\n')
    # Removed local initialization: current_table_rows = []
    
    # Auto-start Cover section for Page 1 if needed
    if page_num == 1 and current_section is None:
        current_section = {
            "section_ID": "Cover",
            "section_title": "Cover",
            "section_generation_order": 0,
            "section_depth": 1,
            "type": "body",
            "page_start": 1,
            "page_end": 1,
            "section_summary": "",
            "section_content": "", 
            "section_image_name_list": [],
            "section_image": [],
            "section_table_list": [],
            "section_table": []
        }
        sections.append(current_section)
    
    for i, line in enumerate(lines):
        header_match = re.match(r'^(#+)\s+(.+)', line)
        
        # New Filter: Ignore headers that start with lowercase (garbage/definitions)
        if header_match:
            title_check = header_match.group(2).strip()
            if title_check and title_check[0].islower():
                logger.debug(f"DEBUG: Ignoring lowercase header: '{title_check}'")
                header_match = None # Treat as not a header

        if header_match:
            # Step A: Close previous section
            if current_section:
                current_section['page_end'] = page_num
                # Generate summary for the completed section
                current_section['section_summary'] = generate_summary_if_needed(current_section['section_content'], current_section['section_title'], current_section['section_ID'])
                if current_table_rows:
                     current_section['section_table'].append(current_table_rows)
                     current_table_rows = []
            
            # Step B: Start new section
            section_counter += 1
            depth = len(header_match.group(1))
            full_header_text = header_match.group(2).strip()
            logger.debug(f"DEBUG: Header found: '{full_header_text}'")

            # Figure/Table Check
            is_figure_or_table = full_header_text.lower().startswith("figure") or full_header_text.lower().startswith("table")
            if is_figure_or_table:
                 logger.debug(f"DEBUG: Ignoring Figure/Table header: {full_header_text}")

            # Section ID Match
            section_match = re.match(r'^([A-Za-z0-9\.]+)\s+(.+)$', full_header_text)
            
            valid_new_section = False
            s_id = None
            s_title = None

            if section_match and not is_figure_or_table:
                s_id = section_match.group(1).rstrip('.') 
                s_title = section_match.group(2).strip()
                
                # --- STRICT VALIDATION AGAINST STRUCTURE ---
                if s_id in section_map:
                    # Check if current page is within allowed range
                    allowed_range = section_map[s_id]
                    if allowed_range['start'] <= page_num <= allowed_range['end']:
                         valid_new_section = True
                         logger.debug(f"DEBUG: Validated Section ID: {s_id} on Page {page_num}")
                    else:
                         logger.debug(f"DEBUG: Section ID {s_id} found on Page {page_num}, but expected {allowed_range}. Treating as content.")
                else:
                    logger.debug(f"DEBUG: Section ID {s_id} NOT found in structure map. Treating as content.")

            if valid_new_section:
                # Step A: Close previous section
                if current_section:
                    current_section['page_end'] = page_num
                    # Generate summary for the completed section
                    current_section['section_summary'] = generate_summary_if_needed(current_section['section_content'], current_section['section_title'], current_section['section_ID'])
                    if current_table_rows:
                         current_section['section_table'].append(current_table_rows)
                         current_table_rows = []
            
                # Step B: Start new section
                section_counter += 1
                depth = len(header_match.group(1))
                logger.debug(f"DEBUG: Starting new Section: {s_id}")

                current_section = {
                    "section_ID": s_id,
                    "section_title": s_title,
                    "section_generation_order": section_counter,
                    "section_depth": depth,
                    "type": "body",
                    "page_start": page_num,
                    "page_end": page_num,
                    "section_summary": "",
                    "section_content": line + "\n", 
                    "section_image_name_list": [],
                    "section_image": [],
                    "section_table_list": [],
                    "section_table": []
                }
                sections.append(current_section)
            else:
                # Not a section header (or is figure), append to previous
                logger.debug(f"DEBUG: Header '{full_header_text}' treated as content.")
                if current_section:
                    current_section['section_content'] += line + "\n"

        
        else:
            # Fallback: Check for implicit headers (e.g., "B.6.2. Title") if no markdown header found
            # Regex: Starts with (Digits+optional dot) OR (UpperAlphanum+Dot+...) 
            # Excludes "Figure", "Table", "NVM" (no dot), "In" (lowercase)
            implicit_match = re.match(r'^((?:\d+\.?)|(?:[A-Z0-9]+\.[A-Z0-9\.]+))\s+(.+)$', line)
            
            # Additional check to ensure it's not just a sentence starting with an acronym
            if implicit_match and len(line) < 100:
                 s_id = implicit_match.group(1).rstrip('.')
                 s_title = implicit_match.group(2).strip()
                 
                 # Only treat as section if VALIDated
                 if s_id in section_map:
                     allowed_range = section_map[s_id]
                     if allowed_range['start'] <= page_num <= allowed_range['end']:
                         # It is valid! Start new section.
                         if current_section:
                            current_section['page_end'] = page_num
                            current_section['section_summary'] = generate_summary_if_needed(current_section['section_content'], current_section['section_title'], current_section['section_ID'])
                            if current_table_rows:
                                current_section['section_table'].append(current_table_rows)
                                current_table_rows = []
                        
                         logger.debug(f"DEBUG: Implicit Section Found & Validated: {s_id}")
                         section_counter += 1
                         current_section = {
                            "section_ID": s_id,
                            "section_title": s_title,
                            "section_generation_order": section_counter,
                            "section_depth": 1, # Default depth for implicit
                            "type": "body",
                            "page_start": page_num,
                            "page_end": page_num,
                            "section_summary": "",
                            "section_content": line + "\n",
                            "section_image_name_list": [],
                            "section_image": [],
                            "section_table_list": [],
                            "section_table": []
                        }
                         sections.append(current_section)
                         continue # Skip appending as content

            # Step C: Append content to current section
            if current_section:
                current_section['section_content'] += line + "\n"
                
                # Check for images or tables
                # Image metadata: <!-- Figure 1, coordinate:(x1,y1,x2,y2) -->
                img_match = re.search(r'<!--\s*(Figure\s*[\d\.]+|Embeded_Image\s*\d+).*?coordinate:\((\d+),(\d+),(\d+),(\d+)\).*?-->', line)
                if img_match:
                    img_name = img_match.group(1)
                    coords = (int(img_match.group(2)), int(img_match.group(3)), int(img_match.group(4)), int(img_match.group(5)))
                    
                    # Deduplication check (for true images)
                    if img_name in current_section['section_image_name_list']:
                         logger.debug(f"DEBUG: Skipping duplicate image name match {img_name} in section {current_section['section_ID']}")
                         # Stop processing this match
                         img_match = None

                    if img_match:
                        # Check if this "Figure" is actually a table
                        # Look ahead in the next few lines for table syntax "|"
                        is_actually_table = False
                        look_ahead_range = 10 # Check next 10 lines
                        for offset in range(1, look_ahead_range + 1):
                            if i + offset < len(lines):
                                next_line = lines[i + offset].strip()
                                # Ignore empty lines or the figure caption itself
                                if not next_line or next_line.startswith("Figure"):
                                    continue
                                if '|' in next_line and set(next_line) - {'|', '-', ':', ' '}:
                                    is_actually_table = True
                                    break
                                # If we hit a new section or mostly text before a table, give up
                                if len(next_line) > 5 and '|' not in next_line:
                                     # Heuristic: if we see text that isn't a table, assume it's an image description or caption
                                     pass
                        
                        if is_actually_table:
                            logger.debug(f"DEBUG: Classified {img_name} as Table (followed by table syntax).")
                            if img_name not in current_section['section_table_list']:
                                current_section['section_table_list'].append(img_name)
                            # We do NOT add to section_image_name_list or crop image
                        else:
                            # It's a real image
                            if img_name not in current_section['section_image_name_list']:
                                # Crop and encode image, then add BOTH name and image if successful
                                if png_path:
                                    encoded_img = crop_and_encode_image(png_path, coords)
                                    if encoded_img:
                                        current_section['section_image_name_list'].append(img_name)
                                        current_section['section_image'].append(encoded_img)
                                    else:
                                        logger.warning(f"DEBUG: Failed to crop/encode image {img_name}, skipping.")
                            else:
                                 # Already exists (deduplication hit earlier or logical fail safe)
                                 pass

                
                # Table detection
                stripped = line.strip()
                is_content_row = '|' in line and bool(set(stripped) - {'|', '-', ':', ' '})
                is_separator_row = '|' in line and set(stripped).issubset({'|', '-', ':', ' '}) and len(stripped) > 2
                
                is_table_row = is_content_row or is_separator_row
                if is_table_row:
                     # This is a weak check, but okay for a first pass
                    current_table_rows.append(line)
                else:
                    if current_table_rows:
                        current_section['section_table'].append(current_table_rows)
                        current_table_rows = []
    
    # Final flush
    if current_section and current_table_rows:
        current_section['section_table'].append(current_table_rows)


def save_page_md(page_data, page_num, output_folder):
    
    os.makedirs(output_folder, exist_ok=True)
    filename = os.path.join(output_folder, f"page_{page_num:04d}.md")
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(page_data)
    
    logger.info(f"  ✅ 저장: {filename}")
    return filename

def process_single_page(png_path, page_num, OUTPUT_MD_FOLDER, section_map):
    """단일 페이지 처리"""
    print(f"\n📄 Processing Page {page_num}...")
    
    md_filename = os.path.join(OUTPUT_MD_FOLDER, f"page_{page_num:04d}.md")
    
    # Check if MD file already exists
    if os.path.exists(md_filename):
        print(f"  ✅ Existing MD found: {md_filename}. Skipping LLM.")
        with open(md_filename, "r", encoding="utf-8") as f:
            response = f.read()
        
        # 3. 섹션 파싱 (Parse from existing MD)
        parse_sections(response, page_num, section_map, png_path)
        return response, 0
    
    start_time = time.time()
    
    # 1. 이미지 인코딩
    base64_img = encode_image_to_base64(png_path)
    
    # 2. LLM 호출
    logger.info(f"  🔄 LLM 분석 중...")
    response = call_ollama_vision(base64_img, IMPROVED_PROMPT)
    
    if not response:
        logger.error(f"  ❌ Page {page_num}: LLM 응답 없음")
        return None, 0
 
    save_page_md(response, page_num, OUTPUT_MD_FOLDER)
    

    
    # 3. 섹션 파싱
    parse_sections(response, page_num, section_map, png_path)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f"  ⏱️ Page {page_num} Processing Time: {elapsed_time:.2f} sec")
    
    return response, elapsed_time
    
    


def get_sorted_files_with_path(folder_path):
    """파일명 앞 3자리 숫자로 정렬된 전체 경로 리스트 반환"""

    path = Path(folder_path)
    
    if not path.exists():
        logger.error(f"폴더가 존재하지 않습니다: {folder_path}")
        return []
    
    # 파일만 필터링하고 전체 경로 저장
    files = [f for f in path.iterdir() if f.is_file()]
    
    # 파일명 앞 3자리로 정렬 (파일명만 기준으로)
    sorted_files = sorted(files, key=lambda x: x.name[:4])
    
    # Path 객체를 문자열로 변환
    sorted_paths = [str(f) for f in sorted_files]
    
    return sorted_paths


def save_json(data, output_folder):
    """Save data to section_info.json"""
    os.makedirs(output_folder, exist_ok=True)
    json_path = os.path.join(output_folder, "section_info.json")
    
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    logger.info(f"  ✅ JSON Saved: {json_path}")


if __name__ == "__main__":
    logger.info("=" * 60)
    logger.info("PDF → JSON Section Processing (Structure-Aware)")
    logger.info("=" * 60)
    
    start_time = time.time()

    # Load Structure
    if not os.path.exists(PDF_STRUCTURE_PATH):
        logger.error(f"Error: Structure file not found at {PDF_STRUCTURE_PATH}. Run extract_pdf_structure.py first.")
        exit(1)

    with open(PDF_STRUCTURE_PATH, 'r', encoding='utf-8') as f:
        structure = json.load(f)

    # Collect all pages to process
    # Use a set to avoid duplicates, then sort
    all_pages_to_process = set()
    for s in structure:
         # Note: s['end_page'] is inclusive in our new logic? 
         # extract_pdf_structure logic: end_page if end_page >= page_num else page_num
         # It represents the last page of the section.
         # So range is [start, end].
         for p in range(s['start_page'], s['end_page'] + 1):
             all_pages_to_process.add(p)
    
    sorted_pages = sorted(list(all_pages_to_process))
    logger.info(f"Total Unique Pages to Process: {len(sorted_pages)}")
    logger.info(f"Pages: {sorted_pages[:10]} ...")

    # Create a lookup map for strict validation: section_ID -> {start_page, end_page}
    section_map = {}
    for s in structure:
        s_id = s.get('section_id') or s.get('section_ID') # Handle key variations
        if s_id:
            section_map[s_id] = {
                'start': s['start_page'],
                'end': s['end_page']
            }

    # Process Pages
    for i, current_page_num in enumerate(sorted_pages):
        png_filename = f"{current_page_num:04d}_page.png"
        image_path = os.path.join(OUTPUT_PNG_FOLDER, png_filename)
        
        # Render if needed
        if not os.path.exists(image_path):
             logger.info(f"Rendering Page {current_page_num}...")
             try:
                page_imgs = convert_from_path(PDF_PATH, first_page=current_page_num, last_page=current_page_num)
                if page_imgs:
                    page_imgs[0].save(image_path, "PNG")
                else:
                    logger.error(f"❌ Error rendering page {current_page_num}")
                    continue
             except Exception as e:
                 logger.error(f"❌ Exception rendering page {current_page_num}: {e}")
                 continue
        
        # Process Page
        process_single_page(image_path, current_page_num, OUTPUT_MD_FOLDER, section_map)

        # Incremental Save (User Request)
        save_json(sections, OUTPUT_JSON_FOLDER)

    # Finalize
    if current_section and current_table_rows:
         current_section['section_table'].append(current_table_rows)
    
    if current_section:
        current_section['section_summary'] = generate_summary_if_needed(current_section['section_content'], current_section['section_title'], current_section['section_ID'])

    logger.info("\n============================================================")
    logger.info("✅ Full Processing Complete")
    
    end_time = time.time()
    logger.info(f"⏱️ Total Execution Time: {end_time - start_time:.2f} sec")
    logger.info("============================================================")

    # Save Output
    save_json(sections, OUTPUT_JSON_FOLDER)
    logger.info(f"📁 Data saved to {OUTPUT_JSON_FOLDER}")
    
