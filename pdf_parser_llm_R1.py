#"Page 별 MD 출력"


import os
import requests
import time
from pdf2image import convert_from_path
import base64
import json
from pathlib import Path


# --- 설정 ---
OLLAMA_BASE_URL = "http://localhost:11434"
MODEL_NAME = "qwen3-vl:32b-instruct-q4_K_M"
PDF_PATH = "./source_doc/NVM-Express-Base-Specification-Revision-2p3.pdf"
OUTPUT_PNG_FOLDER = "./out/output_png"
OUTPUT_JSON_FOLDER = "./out/output_json"
OUTPUT_MD_FOLDER = "./out/md"
RESULT_TXT_FILE = "./out/output_summary.txt"

os.makedirs(OUTPUT_PNG_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_JSON_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_MD_FOLDER, exist_ok=True)

IMPROVED_PROMPT = """
You are a NVMe specification document parser. Extract structured information from this page image.

**Step 1: Page Identification**
- Extract page number from bottom of page (below horizontal line)
- If Roman numerals (i, ii, iii, iv, ..., xvi, ...) → page_type: "toc"
- If Arabic numerals (1, 2, 3, ..., 150, ...) → page_type: "body"

**Step 2: Content Extraction**
  1. write page number and page type at the top like ===== page_number= 1, page_type= body =====
  2. extract text with markdown formatting.
     if there is a embeded image, check image has its name like Figure 1. 
     if image name exists write image name and coordinate as html remark format  "<!-- Figure 1, coordinate:(x1,y1,x2,y2) -->"
     if image name does not exist, write image information as html remark format  "<!-- Embeded_Image 1, coordinate:(x1,y1,x2,y2) -->"
  3. if you fail to parse the content, just  write "extraction_error"
     
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
        filename = os.path.join(output_folder, f"{i+1:04d}_page.png")
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
        return "extraction_error"


def save_page_md(page_data, page_num, output_folder):
    
    os.makedirs(output_folder, exist_ok=True)
    filename = os.path.join(output_folder, f"page_{page_num:04d}.md")
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(page_data)
    
    print(f"  ✅ 저장: {filename}")
    return filename

def process_single_page(png_path, page_num, OUTPUT_MD_FOLDER):
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
 
    save_page_md(response, page_num, OUTPUT_MD_FOLDER)
    
    


def get_sorted_files_with_path(folder_path):
    """파일명 앞 3자리 숫자로 정렬된 전체 경로 리스트 반환"""

    path = Path(folder_path)
    
    if not path.exists():
        print(f"폴더가 존재하지 않습니다: {folder_path}")
        return []
    
    # 파일만 필터링하고 전체 경로 저장
    files = [f for f in path.iterdir() if f.is_file()]
    
    # 파일명 앞 3자리로 정렬 (파일명만 기준으로)
    sorted_files = sorted(files, key=lambda x: x.name[:4])
    
    # Path 객체를 문자열로 변환
    sorted_paths = [str(f) for f in sorted_files]
    
    return sorted_paths



if __name__ == "__main__":
    print("=" * 60)
    print("PDF → JSON 페이지별 변환 시작")
    print("=" * 60)
    
    # 1. PDF → PNG 변환
    png_files=get_sorted_files_with_path(OUTPUT_PNG_FOLDER)
    if png_files is None:  
      print("\n[Step 1] PDF → PNG 변환")
      png_files = pdf_to_png(PDF_PATH, OUTPUT_PNG_FOLDER)
    
    # 2. 각 페이지 처리
    print(f"\n[Step 2] 페이지별 처리 ({len(png_files)}장)")
    all_pages = []
    
    for i, png_path in enumerate(png_files, start=1):
        if i<607:
            continue
        print(f"\n--- 페이지 {png_path} 처리 시작 ---") 
        page_data = process_single_page(png_path, i, OUTPUT_MD_FOLDER)
       
        # 진행률 표시
        print(f"  진행률: {i}/{len(png_files)} ({i*100//len(png_files)}%)")
        time.sleep(1)  # API 과부하 방지 대기 시간
    
