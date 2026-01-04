import os
import requests
import time
import base64
import logging
from pdf2image import convert_from_path
from PIL import Image
import io

# --- Configuration ---
PDF_PATH = "./source_doc/NVM-Express-Base-Specification-Revision-2p3.pdf"
OUTPUT_PNG_FOLDER = "./out2/output_png"
OUTPUT_MD_FOLDER = "./out2/md"
OLLAMA_BASE_URL = "http://localhost:11434"
MODEL_NAME = "qwen3-vl:32b-instruct-q4_K_M"

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Prompt for Page-level Extraction
PAGE_PARSER_PROMPT = """
You are a NVMe specification document parser. Extract structured information from this page image.

**Instructions:**
1. **Strictly extract text visible in the document.** Do NOT generate, hallucinate, or add any text that is not present in the image.
2. Extract text with markdown formatting:
   - Identify section headings (e.g., '1. Introduction', '1.1 Overview') and format them as Markdown headers (#, ##, ###).
   - Do NOT format the document title or running headers as markdown headers.
   - Do NOT format Figure captions or Table titles as markdown headers (do not use #, ##, ### for them).
   - Do NOT output page metadata header (e.g., `===== page_number=...`).
3. **Image Extraction (CRITICAL):**
   - For EVERY block diagram, schematic, or picture (embedded image) except table, you MUST output a metadata comment line BEFORE the caption or image location.
   - Format: `<!-- Figure [Name], coordinate:(x1,y1,x2,y2) -->`
   - Example: `<!-- Figure 1, coordinate:(100,200,900,800) -->`
   - If the image has no name, use: `<!-- Embeded_Image [Index], coordinate:(x1,y1,x2,y2) -->`
   - *Coordinates must be normalized (0-1000).*
   - **CRITICAL: Do NOT output this metadata for TABLES. Tables must be extracted as Markdown tables.**
4. If parsing fails completely, output "extraction_error".
"""

def pdf_to_png(pdf_path, output_folder):
    """Convert PDF to PNG images."""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF NOT FOUND: {pdf_path}")
    
    os.makedirs(output_folder, exist_ok=True)
    logger.info(f"Checking for existing images in {output_folder}...")

    # We can lazily check if we need to convert. 
    # For now, let's assume if the folder is empty or mismatch we reconvert.
    # But to be safe/simple for now: Just convert.
    # Optimization: count pages. 
    
    # Actually, let's process page by page on demand or batch convert.
    # Batch convert is safer for 'step 1'.
    
    logger.info(f"Converting PDF: {pdf_path} ...")
    images = convert_from_path(pdf_path, dpi=200)
    
    saved_files = []
    for i, img in enumerate(images):
        page_num = i + 1
        filename = os.path.join(output_folder, f"{page_num:04d}_page.png")
        if not os.path.exists(filename):
            img.save(filename, "PNG")
        saved_files.append(filename)
    
    logger.info(f"Verified {len(saved_files)} PNG files.")
    return saved_files

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def call_ollama_vision(image_base64, prompt):
    url = f"{OLLAMA_BASE_URL.rstrip('/')}/api/generate"
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "images": [image_base64],
        "options": {
            "temperature": 0.1,
            "num_ctx": 32768,
            "repeat_penalty": 1.2
        }
    }
    
    try:
        response = requests.post(url, json=payload, timeout=900)
        response.raise_for_status()
        return response.json().get("response", "")
    except Exception as e:
        logger.error(f"LLM Call Failed: {e}")
        return None

def process_single_page(png_path, page_num):
    os.makedirs(OUTPUT_MD_FOLDER, exist_ok=True)
    md_filename = os.path.join(OUTPUT_MD_FOLDER, f"page_{page_num:04d}.md")
    
    if os.path.exists(md_filename):
        logger.info(f"Page {page_num}: Content already exists. Skipping LLM.")
        return

    logger.info(f"Page {page_num}: Calling Vision LLM...")
    
    base64_img = encode_image_to_base64(png_path)
    if not base64_img:
        return

    start_time = time.time()
    response_text = call_ollama_vision(base64_img, PAGE_PARSER_PROMPT)
    elapsed = time.time() - start_time
    
    if response_text:
        with open(md_filename, "w", encoding="utf-8") as f:
            f.write(response_text)
        logger.info(f"Page {page_num}: Saved MD ({elapsed:.2f}s)")
    else:
        logger.error(f"Page {page_num}: Failed to generate content.")

def main():
    logger.info("=== STEP 1: PDF Processing (PDF -> PNG -> MD) ===")
    
    # 1. PDF -> PNG
    png_files = pdf_to_png(PDF_PATH, OUTPUT_PNG_FOLDER)
    
    # 2. Process Each Page
    # (For testing, maybe limit or just run all? The user pipeline implies running all.)
    # Let's run for all generated PNGs.
    
    for i, png_path in enumerate(png_files):
        page_num = i + 1
        if page_num<25:
            continue
        process_single_page(png_path, page_num)

if __name__ == "__main__":
    main()
