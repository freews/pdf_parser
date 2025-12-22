"""
Table of Contents 처리 
목차 파서 - Vision LLM 방식 (개선된 프롬프트)
PDF 1-24 page
"""
import os
import json
import base64
import requests
from pathlib import Path
from pdf2image import convert_from_path
import time
from functools import wraps

os.environ['PYTORCH_ALLOC_CONF'] = 'expandable_segments:True'


def timeit_hms(func):
    """시간 측정 데코레이터"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        hours, rem = divmod(elapsed, 3600)
        minutes, seconds = divmod(rem, 60)
        print(f"⏱️ 실행시간: {int(hours)}시간 {int(minutes)}분 {seconds:.3f}초")
        return result
    return wrapper


def create_toc_prompt(page_num: int):
    """
    목차 전용 프롬프트 - 짧고 명확하게
    """
    return f"""Parse this Table of Contents (NOT a table!) into JSON.

Format: [section_number]  [title] .... [page]

Output JSON array ONLY:
[
  {{"level": 1, "number": "1", "title": "INTRODUCTION", "page": 1}},
  {{"level": 2, "number": "1.1", "title": "Overview", "page": 1}},
  {{"level": 3, "number": "1.1.1", "title": "Title", "page": 1}}
]

Rules:
- level = count dots in number + 1 (e.g., "1.2.3" = level 3)
- Ignore dots (...)
- JSON array only, no explanation"""


def parse_toc_with_vision_llm(image_path: Path, page_num: int,
                               ollama_base_url: str, model: str,
                               timeout: int = 300):
    """
    Vision LLM으로 목차 파싱 (개선된 프롬프트)
    """
    print(f"  📄 페이지 {page_num} Vision LLM 분석 중...")
    
    # 프롬프트 생성
    prompt = create_toc_prompt(page_num)
    
    # 이미지를 base64로 인코딩
    with image_path.open("rb") as f:
        img_b64 = base64.b64encode(f.read()).decode("utf-8")
    
    payload = {
        "model": model,
        "prompt": prompt,
        "images": [img_b64],
        "stream": False,
        "options": {
            "temperature": 0.1
        }
    }
    
    url = ollama_base_url.rstrip("/") + "/api/generate"
    
    try:
        resp = requests.post(url, json=payload, timeout=timeout)
        resp.raise_for_status()
        data = resp.json()
        response_text = data.get("response", str(data))
        
        # 🔍 디버그: 실제 응답 출력
        print(f"\n    --- LLM 응답 (첫 500자) ---")
        print(f"    {response_text[:500]}")
        print(f"    --- 응답 끝 ---\n")
        
        # JSON 추출
        import re
        
        # ```json ... ``` 형식
        json_match = re.search(r'```json\s*(.*?)\s*```', response_text, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
        else:
            # [ ... ] 형식 찾기
            json_match = re.search(r'\[\s*\{.*?\}\s*\]', response_text, re.DOTALL)
            if json_match:
                json_str = json_match.group(0)
            else:
                json_str = response_text.strip()
        
        result = json.loads(json_str)
        
        print(f"    ✅ {len(result)}개 항목 추출")
        return result
        
    except Exception as e:
        print(f"    ❌ 오류: {e}")
        print(f"    응답 타입: {type(response_text) if 'response_text' in locals() else 'N/A'}")
        print(f"    응답 길이: {len(response_text) if 'response_text' in locals() else 'N/A'}")
        return []


@timeit_hms
def parse_toc_from_pdf(pdf_path: Path, toc_pages: list,
                       ollama_base_url: str, model: str,
                       output_dir: Path, dpi: int = 150):
    """
    PDF에서 목차 추출 (Vision LLM 사용)
    """
    
    print(f"\n{'='*60}")
    print(f"📚 목차 파싱 시작")
    print(f"📋 대상 페이지: {toc_pages}")
    print(f"🤖 모델: {model}")
    print(f"{'='*60}\n")
    
    # 1. PDF → 이미지 (목차 페이지만)
    print("[1/3] PDF → 이미지 변환 중...")
    images_dir = output_dir / "toc_images"
    images_dir.mkdir(exist_ok=True)
    
    pages = convert_from_path(str(pdf_path), dpi=dpi, 
                             first_page=min(toc_pages), 
                             last_page=max(toc_pages))
    
    image_paths = []
    for i, page_img in enumerate(pages):
        page_num = min(toc_pages) + i
        img_path = images_dir / f"page_{page_num:03}.png"
        page_img.save(img_path, "PNG")
        image_paths.append(img_path)
    
    print(f"✅ {len(image_paths)}개 페이지 이미지 생성\n")
    
    # 2. Vision LLM으로 각 페이지 파싱
    print("[2/3] Vision LLM으로 목차 파싱 중...")
    all_entries = []
    
    for i, img_path in enumerate(image_paths):
        page_num = min(toc_pages) + i
        
        entries = parse_toc_with_vision_llm(
            img_path, page_num, ollama_base_url, model, timeout=1200  # 20분
        )
        
        # 페이지 정보 추가
        for entry in entries:
            entry['source_page'] = page_num
        
        all_entries.extend(entries)
        
        # 미리보기 (처음 3개만)
        if entries:
            print(f"    미리보기:")
            for entry in entries[:3]:
                indent = "  " * (entry.get('indent_level', 1) - 1)
                section = entry.get('section_number', '')
                title = entry.get('title', '')
                page = entry.get('page', '?')
                print(f"      {indent}{section} {title} ... {page}")
        print()
    
    # 3. 결과 저장
    print("[3/3] 결과 저장 중...")
    
    # JSON 저장
    json_path = output_dir / "toc_parsed.json"
    with json_path.open('w', encoding='utf-8') as f:
        json.dump(all_entries, f, ensure_ascii=False, indent=2)
    print(f"✅ JSON 저장: {json_path}")
    
    # Markdown 저장
    md_path = output_dir / "toc_parsed.md"
    with md_path.open('w', encoding='utf-8') as f:
        f.write("# Table of Contents\n\n")
        
        for entry in all_entries:
            # 양쪽 키 모두 지원
            indent = entry.get('indent_level') or entry.get('level', 1)
            section = entry.get('section_number') or entry.get('number', '')
            title = entry.get('title', '')
            page = entry.get('page', '?')
            
            indent_str = "  " * (indent - 1)
            
            if section:
                f.write(f"{indent_str}- **{section}** {title} `..... page {page}`\n")
            else:
                f.write(f"{indent_str}- {title} `..... page {page}`\n")
    
    print(f"✅ Markdown 저장: {md_path}")
    
    # 통계
    print(f"\n{'='*60}")
    print(f"✅ 파싱 완료!")
    print(f"{'='*60}")
    print(f"📊 총 항목 수: {len(all_entries)}")
    print(f"📊 레벨별 통계:")
    
    from collections import Counter
    level_counts = Counter(entry.get('indent_level') or entry.get('level', 0) for entry in all_entries)
    for level in sorted(level_counts.keys()):
        print(f"   레벨 {level}: {level_counts[level]}개")
    
    print(f"{'='*60}\n")
    
    return all_entries, json_path, md_path


def main():
    """메인 함수"""
    
    # ==================== 설정 ====================
    PDF_PATH = Path("./source_doc/nvme_short.pdf")
    OUTPUT_DIR = Path("./out/toc_vision")
    Path.mkdir(OUTPUT_DIR, exist_ok=True)

    
    TOC_PAGES = [1, 24] 
    
    # Vision LLM 설정
    MODEL = "qwen3-vl:30b-a3b-instruct-q4_K_M"
    OLLAMA_BASE_URL = "http://localhost:11434"
    DPI = 200  # 낮춰서 더 빠르게
    # ===============================================
    
    if not PDF_PATH.exists():
        print(f"❌ PDF 파일을 찾을 수 없습니다: {PDF_PATH}")
        return
    
    # 목차 파싱 실행
    entries, json_path, md_path = parse_toc_from_pdf(
        pdf_path=PDF_PATH,
        toc_pages=TOC_PAGES,
        ollama_base_url=OLLAMA_BASE_URL,
        model=MODEL,
        output_dir=OUTPUT_DIR,
        dpi=DPI
    )
    
    print(f"🎉 완료! 결과 확인:")
    print(f"   JSON: {json_path}")
    print(f"   Markdown: {md_path}")


if __name__ == "__main__":
    main()