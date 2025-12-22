import os
import requests
import time
from pdf2image import convert_from_path
import base64
import json


# --- 설정 ---
OLLAMA_BASE_URL = "http://localhost:11434"
MODEL_NAME = "qwen3-vl:32b-instruct-q4_K_M"
PDF_PATH = "./source_doc/NVM-Express-Base-Specification-Revision-2p3.pdf"
OUTPUT_PNG_FOLDER = "./rag2/output_png"
OUTPUT_JSON_FOLDER = "./rag2/output_json"
RESULT_TXT_FILE = "./rag2/output_summary.txt"

os.makedirs(OUTPUT_PNG_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_JSON_FOLDER, exist_ok=True)

IMPROVED_PROMPT = """
You are a NVMe specification document parser. Extract structured information from this page image.

**Step 1: Page Identification**
- Extract page number from bottom of page (below horizontal line)
- If Roman numerals (i, ii, iii, iv, ..., xvi, ...) → page_type: "toc"
- If Arabic numerals (1, 2, 3, ..., 150, ...) → page_type: "body"

**Step 2: Content Extraction**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FOR TOC PAGES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Parse entries with pattern: "ItemID: Title ........... PageNumber"

Examples:
- "Figure 372: Set Controller State – Command Dword 13.........383"
  → {id: "Figure 372", type: "figure", title: "Set Controller State – Command Dword 13", target_page: "383"}
- "Table 35: NVMe Admin Command Set.........150"
  → {id: "Table 35", type: "table", title: "NVMe Admin Command Set", target_page: "150"}

Extract ALL entries into toc_entries array.

Output format:
{
  "page_number": "xvi",
  "page_type": "toc",
  "toc_entries": [
    {
      "id": "Figure 372",
      "type": "figure" or "table",
      "title": "Set Controller State – Command Dword 13",
      "target_page": "383"
    }
  ],
  "metadata": {
    "total_entries": count,
    "raw_content": "full markdown backup"
  }
}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FOR BODY PAGES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

**1. Section Information**
- Find section heading (### 1.4.3 Byte, Word, and Dword Relationships)
- Extract: section number, title, level (count # symbols)

**2. Text Content**
- Extract all text EXCLUDING figures and tables
- Keep section structure and subsections
- Replace figure/table locations with references: [Figure 3] or [Table 35]

**3. Figures and Tables**

IMPORTANT: Figures can be two types:
A. Visual diagrams/images → Has bounding box coordinates
B. Formatted as tables → Has markdown table structure

For each Figure/Table found:

IF it's a visual diagram:
{
  "id": "Figure 3",
  "title": "Byte, Word, and Dword Relationships",
  "type": "image",
  "has_coordinates": true,
  "coordinates": [x0, y0, x1, y1],
  "description": "brief description if available"
}

IF it's formatted as a table:
{
  "id": "Figure 372" or "Table 35",
  "title": "...",
  "type": "table",
  "has_coordinates": false,
  "coordinates": null,
  "markdown_content": "| Header1 | Header2 |\\n|---------|---------|\\n| data1   | data2   |",
  "continues_next_page": true/false
}

**4. Continuation Detection**
- Check if table title contains "(continued)"
  → If yes: "is_continuation": true
- Check if table ends at page bottom (incomplete)
  → If yes: "continues_next_page": true

Output format:
{
  "page_number": "5",
  "page_type": "body",
  "section": {
    "number": "1.4.3",
    "title": "Byte, Word, and Dword Relationships",
    "level": 3
  },
  "text_content": "Full text without figures/tables. Use [Figure 3] for references.",
  "figures": [
    {
      "id": "Figure 3",
      "title": "...",
      "type": "image" or "table",
      "has_coordinates": true/false,
      "coordinates": [...] or null,
      "markdown_content": "..." or null (only for type: table),
      "continues_next_page": false
    }
  ],
  "tables": [],
  "metadata": {
    "has_subsections": true/false,
    "subsections": ["1.5", "1.5.1"],
    "references": ["Figure 3", "Table 35"],
    "has_continuation": false
  }
}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CRITICAL RULES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Output ONLY valid JSON, no markdown code blocks
2. Separate text, figures, and tables completely
3. Preserve all markdown formatting in text_content
4. Extract accurate coordinates for images
5. Convert tables to proper markdown format
6. Detect table continuation accurately
7. Keep references in text like [Figure 3]
8. Extract ALL TOC entries completely
9. Handle 3-column TOC layout (item, title, page)
10. No summarization - include ALL content

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""


def pdf_to_png(pdf_path, output_folder):
    """PDF를 PNG 이미지로 변환"""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF 파일을 찾을 수 없습니다: {pdf_path}")
    
    os.makedirs(output_folder, exist_ok=True)
    print(f"🔄 PDF 변환 중: {pdf_path}")
    
    images = convert_from_path(pdf_path, dpi=200)
    png_files = []
    
    for i, img in enumerate(images):
        filename = os.path.join(output_folder, f"page_{i+1:04d}.png")
        img.save(filename, "PNG")
        png_files.append(filename)
    
    print(f"✅ {len(images)}장의 PNG 이미지 생성 완료 → {output_folder}")
    return png_files


def encode_image_to_base64(image_path):
    """이미지를 base64로 인코딩"""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")


def call_ollama_vision(image_base64, prompt):
    """Ollama Vision API 호출 (단일 이미지)"""
    url = f"{OLLAMA_BASE_URL.rstrip('/')}/api/generate"
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "images": [image_base64],
        "options": {
            "temperature": 0.1
        }
    }
    
    try:
        response = requests.post(url, json=payload, timeout=900)
        response.raise_for_status()
        result = response.json()
        return result.get("response", "")
    except Exception as e:
        print(f"❌ LLM 호출 실패: {e}")
        return None


def extract_json_from_response(response_text):
    """응답에서 JSON 추출 (코드 블록 제거)"""
    # ```json ... ``` 형식 처리
    if "```json" in response_text:
        start = response_text.find("```json") + 7
        end = response_text.find("```", start)
        json_text = response_text[start:end].strip()
    elif "```" in response_text:
        start = response_text.find("```") + 3
        end = response_text.find("```", start)
        json_text = response_text[start:end].strip()
    else:
        json_text = response_text.strip()
    
    try:
        return json.loads(json_text)
    except json.JSONDecodeError as e:
        print(f"⚠️ JSON 파싱 실패: {e}")
        print(f"응답 내용: {response_text[:200]}...")
        return None


def save_page_json(page_data, page_num, output_folder):
    """페이지별 JSON 파일 저장"""
    os.makedirs(output_folder, exist_ok=True)
    filename = os.path.join(output_folder, f"page_{page_num:04d}.json")
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(page_data, f, ensure_ascii=False, indent=2)
    
    print(f"  ✅ 저장: {filename}")
    return filename


def save_summary(all_pages, filename):
    """전체 페이지 요약 저장"""
    summary = {
        "total_pages": len(all_pages),
        "pages": all_pages
    }
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 전체 요약 저장: {filename}")


def process_single_page(png_path, page_num, output_json_folder):
    """단일 페이지 처리"""
    print(f"\n📄 Processing Page {page_num}...")
    
    # 1. 이미지 인코딩
    base64_img = encode_image_to_base64(png_path)
    
    # 2. LLM 호출
    print(f"  🔄 LLM 분석 중...")
    response = call_ollama_vision(base64_img, IMPROVED_PROMPT)
    
    if not response:
        print(f"  ❌ Page {page_num}: LLM 응답 없음")
        return None
    
    # 3. JSON 추출
    page_data = extract_json_from_response(response)
    
    if not page_data:
        print(f"  ❌ Page {page_num}: JSON 파싱 실패")
        # 원본 응답이라도 저장
        page_data = {
            "page_number": page_num,
            "page_type": "unknown",
            "content": response,
            "metadata": {
                "embedded_images": [],
                "parse_error": True
            }
        }
    
    # 4. 페이지 번호 보정 (응답에 없으면 추가)
    if "page_number" not in page_data:
        page_data["page_number"] = page_num
    
    # 5. JSON 파일 저장
    save_page_json(page_data, page_num, output_json_folder)
    
    return page_data


if __name__ == "__main__":
    print("=" * 60)
    print("PDF → JSON 페이지별 변환 시작")
    print("=" * 60)
    
    # 1. PDF → PNG 변환
    print("\n[Step 1] PDF → PNG 변환")
    png_files = pdf_to_png(PDF_PATH, OUTPUT_PNG_FOLDER)
    
    # 2. 각 페이지 처리
    print(f"\n[Step 2] 페이지별 처리 ({len(png_files)}장)")
    all_pages = []
    
    for i, png_path in enumerate(png_files, start=1):
        page_data = process_single_page(png_path, i, OUTPUT_JSON_FOLDER)
        
        if page_data:
            all_pages.append({
                "page_number": page_data.get("page_number", i),
                "page_type": page_data.get("page_type", "unknown"),
                "json_file": f"page_{i:04d}.json"
            })
        
        # 진행률 표시
        print(f"  진행률: {i}/{len(png_files)} ({i*100//len(png_files)}%)")
        time.sleep(5)  # API 과부하 방지 대기 시간
    
    # 3. 전체 요약 저장
    print("\n[Step 3] 전체 요약 생성")
    save_summary(all_pages, "output_summary.json")
    
    print("\n" + "=" * 60)
    print("✅ 모든 처리 완료!")
    print(f"  - PNG 파일: {OUTPUT_PNG_FOLDER}/")
    print(f"  - JSON 파일: {OUTPUT_JSON_FOLDER}/")
    print(f"  - 요약 파일: output_summary.json")
    print("=" * 60)