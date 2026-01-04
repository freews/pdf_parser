import json
import os
import re
import logging
import base64
import io
from functools import lru_cache
from pdf2image import convert_from_path
from PIL import Image
from html.parser import HTMLParser

# --- Configuration ---
STRUCTURE_FILE = "./out/pdf_structure.json"
MD_FOLDER = "./out/md"
OUTPUT_JSON = "./out/section_content.json"
PDF_PATH = "./source_doc/NVM-Express-Base-Specification-Revision-2p3.pdf"

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Increase max image size
Image.MAX_IMAGE_PIXELS = None


class TableToMarkdownParser(HTMLParser):
    """HTML table을 Markdown 형식으로 변환 (단순화 버전)"""
    
    def __init__(self):
        super().__init__()
        self.rows = []
        self.current_row = []
        self.current_cell = []
        self.in_th_td = False
        self.current_row_is_header = True
        self.row_types = []

    def handle_starttag(self, tag, attrs):
        tag_lower = tag.lower()
        
        if tag_lower == 'tr':
            self.current_row = []
            self.current_row_is_header = True
        elif tag_lower in ('th', 'td'):
            self.in_th_td = True
            self.current_cell = []
            if tag_lower == 'td':
                self.current_row_is_header = False

    def handle_endtag(self, tag):
        tag_lower = tag.lower()
        
        if tag_lower == 'tr':
            if self.current_row:
                self.rows.append(self.current_row)
                self.row_types.append('header' if self.current_row_is_header else 'data')
        elif tag_lower in ('td', 'th'):
            self.in_th_td = False
            cell_content = " ".join(self.current_cell).strip()
            cell_content = re.sub(r'\s+', ' ', cell_content)
            self.current_row.append(cell_content)

    def handle_data(self, data):
        if self.in_th_td:
            self.current_cell.append(data)

    def get_markdown(self):
        """변환된 Markdown 테이블 반환"""
        if not self.rows:
            return ""
        
        md_lines = []
        for i, row in enumerate(self.rows):
            md_line = "| " + " | ".join(row) + " |"
            md_lines.append(md_line)
            
            if self.row_types[i] == 'header':
                sep = "| " + " | ".join(['---'] * len(row)) + " |"
                md_lines.append(sep)
        
        return "\n".join(md_lines)


def process_html_tables(content):
    """HTML 테이블을 Markdown으로 변환 (단순화 버전)"""
    processed_content = content
    start_search_idx = 0
    
    while True:
        # <table 찾기
        table_start = re.search(r'<table', processed_content[start_search_idx:], re.IGNORECASE)
        if not table_start:
            break
        
        start_idx = start_search_idx + table_start.start()
        
        # </table> 찾기
        table_end = re.search(r'</table>', processed_content[start_idx:], re.IGNORECASE)
        if not table_end:
            # 짝이 없으면 다음으로 이동
            start_search_idx = start_idx + 1
            continue
        
        end_idx = start_idx + table_end.end()
        
        # HTML 테이블 추출 및 Markdown으로 변환
        table_html = processed_content[start_idx:end_idx]
        parser = TableToMarkdownParser()
        parser.feed(table_html)
        md_table = parser.get_markdown()
        
        # 변환된 내용으로 교체
        processed_content = (processed_content[:start_idx] + 
                           "\n" + md_table + "\n" + 
                           processed_content[end_idx:])
        
        start_search_idx = start_idx + len(md_table) + 2
    
    return processed_content


def load_json(path):
    """JSON 파일 로드"""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def read_page_md(page_num):
    """페이지별 Markdown 파일 읽기 및 HTML 테이블 전처리"""
    path = os.path.join(MD_FOLDER, f"page_{page_num:04d}.md")
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content_raw = f.read()
        return process_html_tables(content_raw)
    return ""


# 성능 개선: 페이지 이미지 캐싱 (LRU 캐시로 최근 5개 페이지만 유지)
@lru_cache(maxsize=5)
def get_page_image(pdf_path, page_num, dpi=200):
    """PDF 페이지를 이미지로 렌더링 (캐싱됨)"""
    try:
        images = convert_from_path(pdf_path, dpi=dpi, first_page=page_num, last_page=page_num)
        return images[0] if images else None
    except Exception as e:
        logger.error(f"❌ Failed to render page {page_num}: {e}")
        return None


def crop_and_encode_image(pdf_path, page_num, coords):
    """이미지 크롭 및 base64 인코딩"""
    try:
        img = get_page_image(pdf_path, page_num)
        if not img:
            return None
        
        width, height = img.size
        
        # 좌표 정규화 (0-1000 -> pixels)
        x1 = int(coords[0] * width / 1000)
        y1 = int(coords[1] * height / 1000)
        x2 = int(coords[2] * width / 1000)
        y2 = int(coords[3] * height / 1000)
        
        if x1 >= x2 or y1 >= y2:
            logger.warning(f"⚠️ Invalid coordinates: {coords} on page {page_num}")
            return None

        cropped_img = img.crop((x1, y1, x2, y2))
        
        buffered = io.BytesIO()
        cropped_img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode("utf-8")
        
    except Exception as e:
        logger.error(f"❌ Image crop failed on page {page_num}: {e}")
        return None


def is_table_content(line):
    """라인이 테이블 내용인지 확인"""
    stripped = line.strip()
    if '|' not in line:
        return False
    
    # 내용이 있는 행
    if set(stripped) - {'|', '-', ':', ' '}:
        return True
    
    # 구분자 행
    if set(stripped).issubset({'|', '-', ':', ' '}) and len(stripped) > 2:
        return True
    
    return False


def extract_figure_caption(line):
    """Figure 캡션 추출 (예: 'Figure 5', 'Figure 123', 'Table 3')"""
    # Figure/Table 번호 추출
    match = re.search(r'\b(Figure|Table)\s+(\d+)', line, re.IGNORECASE)
    if match:
        return f"{match.group(1)} {match.group(2)}"
    return None


def extract_section_content_and_assets(section, next_section=None):
    """섹션의 컨텐츠, 이미지, 테이블 추출"""
    content_buffer = []
    section_images = {}  # {figure_name: base64_image}
    section_tables = {}  # {figure_name: [markdown_rows]}
    
    start_page = section['start_page']
    end_page = section['end_page']
    sec_id = section['section_id']
    
    logger.info(f"Processing Section {sec_id}: Pages {start_page}-{end_page}")

    current_table_rows = []
    current_figure_name = None  # 현재 처리 중인 Figure 이름

    for p in range(start_page, end_page + 1):
        page_content = read_page_md(p)
        
        if not page_content:
            logger.warning(f"  Page {p} content missing.")
            continue
        
        lines = page_content.split('\n')
        
        # --- 페이지 필터링 ---
        if p == start_page:
            header_pattern = re.compile(
                rf'^(\#+|\*\*)\s*{re.escape(sec_id)}\.?\s*.*', 
                re.IGNORECASE
            )
            for i, line in enumerate(lines):
                if header_pattern.match(line):
                    lines = lines[i:]
                    break
        
        if p == end_page and next_section and next_section['start_page'] == end_page:
            next_id = next_section['section_id']
            next_pattern = re.compile(
                rf'^(\#+|\*\*)\s*{re.escape(next_id)}\.?\s*.*', 
                re.IGNORECASE
            )
            for i, line in enumerate(lines):
                if next_pattern.match(line):
                    lines = lines[:i]
                    break
        
        # --- 에셋 추출 ---
        processed_lines = []
        
        for i, line in enumerate(lines):
            # Figure 캡션 감지
            fig_caption = extract_figure_caption(line)
            if fig_caption:
                current_figure_name = fig_caption
            
            # 이미지 메타데이터 감지 (실제 이미지인 경우)
            img_match = re.search(
                r'<!--\s*(Figure\s*[\d\.]+|Embeded_Image\s*\d+).*?'
                r'coordinate:\((\d+),(\d+),(\d+),(\d+)\).*?-->', 
                line
            )
            
            if img_match:
                img_name = img_match.group(1)
                coords = tuple(int(img_match.group(j)) for j in range(2, 6))
                
                # 실제 이미지 추출
                if img_name not in section_images:
                    logger.info(f"  Extracting Image: {img_name} from Page {p}")
                    b64_img = crop_and_encode_image(PDF_PATH, p, coords)
                    if b64_img:
                        section_images[img_name] = b64_img
                
                # 메타데이터 라인은 content에서 제거
                continue
            
            # 테이블 행 수집
            if is_table_content(line):
                current_table_rows.append(line)
            else:
                # 테이블 종료 시 저장
                if len(current_table_rows) > 1 and current_figure_name:
                    # Figure 이름으로 테이블 머지
                    if current_figure_name in section_tables:
                        # 기존 테이블에 추가 (헤더 제외하고 병합)
                        existing_rows = section_tables[current_figure_name]
                        # 헤더와 구분자 건너뛰기
                        start_idx = 2 if len(current_table_rows) > 1 and \
                                    set(current_table_rows[1].strip()).issubset({'|', '-', ':', ' '}) else 1
                        existing_rows.extend(current_table_rows[start_idx:])
                        logger.info(f"  Merged table rows to {current_figure_name} (Page {p})")
                    else:
                        section_tables[current_figure_name] = current_table_rows.copy()
                        logger.info(f"  Collected table: {current_figure_name} (Page {p})")
                
                current_table_rows = []
            
            processed_lines.append(line)
        
        # 페이지 끝에 남은 테이블 처리
        if len(current_table_rows) > 1 and current_figure_name:
            if current_figure_name in section_tables:
                existing_rows = section_tables[current_figure_name]
                start_idx = 2 if len(current_table_rows) > 1 and \
                            set(current_table_rows[1].strip()).issubset({'|', '-', ':', ' '}) else 1
                existing_rows.extend(current_table_rows[start_idx:])
                logger.info(f"  Merged table rows to {current_figure_name} (Page {p}, end)")
            else:
                section_tables[current_figure_name] = current_table_rows.copy()
                logger.info(f"  Collected table: {current_figure_name} (Page {p}, end)")
        
        current_table_rows = []
        
        content_buffer.append("\n".join(processed_lines))

    # content_md 생성 (테이블 본문 제거)
    full_content = "\n\n".join(content_buffer)
    
    # 테이블 본문을 content에서 제거 (참조는 유지)
    for line in full_content.split('\n'):
        if is_table_content(line):
            full_content = full_content.replace(line, '')
    
    # 빈 줄 정리
    full_content = re.sub(r'\n{3,}', '\n\n', full_content)
    
    # 리스트 형식으로 변환
    image_names = list(section_images.keys())
    image_data = list(section_images.values())
    table_names = list(section_tables.keys())
    table_data = list(section_tables.values())
    
    return full_content, image_names, image_data, table_names, table_data


def main():
    logger.info("=== STEP 3: Section Aggregation with Asset Extraction (Improved) ===")
    
    if not os.path.exists(STRUCTURE_FILE):
        logger.error("Structure file missing. Run step2_extract_pdf_structure.py first.")
        return

    if not os.path.exists(PDF_PATH):
        logger.error(f"PDF missing at {PDF_PATH}. Cannot extract images.")
        return

    structure = load_json(STRUCTURE_FILE)
    output_data = []
    
    total = len(structure)
    for i, section in enumerate(structure):
        title = section.get('title', 'Unknown')
        start_page = section.get('start_page', 0)
        
        # # 첫 장과 25페이지부터 끝까지만 처리
        # if start_page > 1 and start_page < 25:
        #     logger.info(f"[{i+1}/{total}] Skipping: {title} (Page {start_page})")
        #     continue
        
        logger.info(f"[{i+1}/{total}] Aggregating: {title}")

        next_sec = structure[i+1] if i < len(structure) - 1 else None
        content, img_names, imgs, tbl_names, tbls = extract_section_content_and_assets(section, next_sec)
        
        section_entry = section.copy()
        section_entry.update({
            'content_md': content,
            'section_image_name_list': img_names,
            'section_image': imgs,
            'section_table_list': tbl_names,
            'section_table': tbls,
            'summary': ""
        })
        
        output_data.append(section_entry)

        # 10개 섹션마다 저장
        if (i + 1) % 10 == 0:
            with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
                json.dump(output_data, f, indent=4, ensure_ascii=False)
            logger.info(f"Progress saved ({i+1}/{total})")

    # 최종 저장
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)
    
    logger.info(f"✅ Saved to {OUTPUT_JSON}")
    logger.info(f"✅ Processed {len(output_data)} sections")


if __name__ == "__main__":
    main()
