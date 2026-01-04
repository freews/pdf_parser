import json
import requests
import os
import logging

# --- Configuration ---
INPUT_JSON = "./out/section_content.json"
OUTPUT_JSON = "./out/section_content.json"  # Save back to the same file
OLLAMA_BASE_URL = "http://localhost:11434"
MODEL_NAME = "qwen3-vl:32b-instruct-q4_K_M"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def generate_summary(text, section_title):
    """섹션 내용에 대한 한국어 요약 생성"""
    if len(text) < 200:
        return text  # 너무 짧으면 원문 그대로 사용
        
    prompt = f"""당신은 NVMe 규격 문서 전문가입니다.
섹션: {section_title}

다음 기술 문서 내용을 한국어로 3-5문장으로 요약해주세요.
목적, 요구사항, 주요 정의사항에 초점을 맞춰주세요.

내용:
{text[:15000]} 

요약 (한국어):"""
    
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
        response = requests.post(f"{OLLAMA_BASE_URL}/api/generate", json=payload, timeout=300)
        return response.json().get("response", "").strip()
    except Exception as e:
        logger.error(f"요약 생성 실패: {e}")
        return "요약 생성 실패."

def main():
    logger.info("=== STEP 4: 한국어 요약 생성 ===")
    
    if not os.path.exists(INPUT_JSON):
        logger.error("입력 JSON 파일이 없습니다.")
        return

    with open(INPUT_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for i, section in enumerate(data):
        t = section.get('title', 'Unknown')
        id = section.get('section_id', 'Unknown')
        start_page = section.get('start_page', 0)
        
        # 첫 장과 25페이지부터 끝까지만 처리
        if start_page > 1 and start_page < 25:
            logger.info(f"건너뛰기: {id}:{t} (Page {start_page})")
            continue
        
        # 이미 요약된 경우 건너뛰기
        if section.get('summary'):
            logger.info(f"이미 요약됨: {id}:{t}")
            continue

        c = section.get('content_md', '')
        
        if c:
            logger.info(f"요약 생성 중: {id}:{t}...")
            section['summary'] = generate_summary(c, t)
        else:
            section['summary'] = "(내용 없음)"
        
        # 진행 상황 저장 (섹션별로)
        temp_file = OUTPUT_JSON + ".tmp"
        try:
            with open(temp_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            os.replace(temp_file, OUTPUT_JSON)
            logger.info(f"진행 상황 저장: {t}")
        except Exception as e:
            logger.error(f"저장 실패: {e}")

    logger.info(f"완료. 모든 요약이 {OUTPUT_JSON}에 저장되었습니다.")

if __name__ == "__main__":
    main()
