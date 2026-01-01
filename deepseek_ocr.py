import requests
import base64
import json,os,time
from pathlib import Path
import logger

os.environ['PYTORCH_ALLOC_CONF'] = 'expandable_segments:True'

def deepseek_ocr(image_path, mode="free"):
    """
    mode 옵션:
    - "free": 단순 텍스트 추출
    - "layout": 레이아웃 정보 포함
    - "markdown": 마크다운 변환
    - "figure": 도표/차트 파싱
  
    """
    
    # 프롬프트 템플릿 (줄바꿈과 구두점 중요!)
    prompts = {
        "free": "Free OCR.",
        "layout": "<|grounding|>Given the layout of the image.",
        "markdown": "<|grounding|>Convert the document to markdown.",
        "figure": "Parse the figure.",
        "extract": "Extract the text in the image."
    }
    
    # 이미지를 base64로 인코딩
    with open(image_path, 'rb') as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')
    
    url = "http://localhost:11434/api/generate"
    
    # 중요: 프롬프트는 줄바꿈(\n)을 포함해야 함
    data = {
        "model": "deepseek-ocr:latest",
        "prompt": f"\n{prompts[mode]}",
        "images": [image_data],
        "stream": False,
        "options": {
            "temperature": 0  # OCR은 온도 0 권장
        }
    }
    
    response = requests.post(url, json=data)
    return response.json()['response']

#   # 사용 예제
# result = deepseek_ocr("out/output_png/0003_page.png", mode="markdown")
# print(result)


class DeepSeekOCR:
    def __init__(self, base_url="http://localhost:11434", model="deepseek-ocr:latest"):
        self.base_url = base_url
        self.model = model
    
    def _encode_image(self, image_path):
        """이미지를 base64로 인코딩"""
        with open(image_path, 'rb') as f:
            return base64.b64encode(f.read()).decode('utf-8')
    
    def _call_api(self, image_path, prompt_suffix, stream=False):
        """API 호출 (프롬프트 형식 주의)"""
        image_b64 = self._encode_image(image_path)
        
        # 줄바꿈 포함 필수!
        full_prompt = f"\n{prompt_suffix}"
        
        data = {
            "model": self.model,
            "prompt": full_prompt,
            "images": [image_b64],
            "stream": stream,
            "options": {
                "temperature": 0
            }
        }
        try:
            response = requests.post(
                f"{self.base_url}/api/generate", 
                json=data, 
                stream=stream
            )
        except requests.exceptions.RequestException as e:
            print(f"API 요청 중 오류 발생: {e}")
            logger.logger.error(f"API 요청 중 오류 발생: {e}")  
            return None
        
        if stream:
            result = ""
            for line in response.iter_lines():
                if line:
                    chunk = json.loads(line)
                    if not chunk.get('done'):
                        text = chunk.get('response', '')
                        print(text, end='', flush=True)
                        result += text
            print()
            return result
        else:
            return response.json()['response']
    
    def free_ocr(self, image_path, stream=False):
        """단순 텍스트 추출"""
        return self._call_api(image_path, "Free OCR.", stream)
    
    def extract_text(self, image_path, stream=False):
        """이미지 내 텍스트 추출"""
        return self._call_api(image_path, "Extract the text in the image.", stream)
    
    def with_layout(self, image_path, stream=False):
        """레이아웃 정보와 함께 추출"""
        return self._call_api(image_path, "<|grounding|>Given the layout of the image.", stream)
    
    def to_markdown(self, image_path, stream=False):
        """마크다운 형식으로 변환"""
        return self._call_api(image_path, "<|grounding|>Convert the document to markdown.", stream)
    
    def parse_figure(self, image_path, stream=False):
        """도표/차트 파싱"""
        return self._call_api(image_path, "Parse the figure.", stream)

# # 사용 예제
# ocr = DeepSeekOCR()

# # 기본 OCR
# png_path="source_doc/nvme_short.pdf"
# text = ocr.free_ocr(pdf_path)
# print(text)

# # 마크다운 변환 (스트리밍)
# print("=== 마크다운 변환 (스트리밍) ===")
# markdown = ocr.to_markdown("document.png", stream=True)

# # 레이아웃 정보 포함
# layout_text = ocr.with_layout("table.png")
# print(layout_text)





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

source_img_dir="out/output_png"
result_dir="out_deepseek/layout"
os.makedirs(result_dir, exist_ok=True)  

images=get_sorted_files_with_path(source_img_dir)
ocr = DeepSeekOCR()
for img in images:
    page=img.split('_')[1].split('/')[1]
    # if int(page)<29:#page 29 에서 중단됨
    #     continue

    logger.logger.info(f"Processing image start: {img}")
    
    # result = ocr.to_markdown(img)
    # if result is None:
    #     result = f"Error: OCR failed at page {page}."
    # with open(f"{result_dir}/{Path(img).stem}.md", "w", encoding="utf-8") as f:
    #     f.write(result) 

    result = ocr.with_layout(img)
    if result is None:
        result = f"Error: OCR failed at page {page}."
    with open(f"{result_dir}/{Path(img).stem}.txt", "w", encoding="utf-8") as f:
        f.write(result)     

  #  print(f"Processing image end: {result}")
    logger.logger.info(f"Processing image end: {result}")
    time.sleep(2)  # 너무 빠른 요청을 피하기 위해 잠시 대기