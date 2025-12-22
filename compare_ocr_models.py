import os
import time
import json
import base64
import requests
from pathlib import Path
from pdf2image import convert_from_path

# Configuration
PDF_PATH = "source_doc/nvme_short.pdf"
OUTPUT_DIR = "out_compare"
DEEPSEEK_MODEL = "deepseek-ocr:latest"
QWEN_MODEL = "qwen3-vl:32b-instruct-q4_K_M"
OLLAMA_BASE_URL = "http://localhost:11434"

# Ensure output directories exist
os.makedirs(os.path.join(OUTPUT_DIR, "deepseek", "md"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "deepseek", "txt"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "qwen", "md"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "qwen", "txt"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "images"), exist_ok=True)

def pdf_to_png(pdf_path, output_folder):
    """Convert PDF to PNG images."""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
    
    print(f"Converting PDF: {pdf_path}")
    # Check if images already exist to save time? 
    # For now, let's just convert to be safe and ensure matching filenames.
    images = convert_from_path(pdf_path, dpi=200)
    png_files = []
    
    for i, img in enumerate(images):
        filename = os.path.join(output_folder, f"page_{i+1:04d}.png")
        img.save(filename, "PNG")
        png_files.append(filename)
    
    print(f"Converted {len(images)} pages.")
    return png_files

def encode_image(image_path):
    """Encode image to base64."""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def call_ollama(model, prompt, image_path, stream=False):
    """Generic Ollama API call."""
    url = f"{OLLAMA_BASE_URL.rstrip('/')}/api/generate"
    image_b64 = encode_image(image_path)
    
    data = {
        "model": model,
        "prompt": prompt,
        "images": [image_b64],
        "stream": stream,
        "options": {
            "temperature": 0
        }
    }
    
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json().get('response', '')
    except Exception as e:
        print(f"Error calling {model}: {e}")
        return None

def deepseek_process(image_path):
    """Process with DeepSeek OCR."""
    # Using 'markdown' mode prompt from reference
    prompt = "\n<|grounding|>Convert the document to markdown."
    return call_ollama(DEEPSEEK_MODEL, prompt, image_path)

def qwen_process(image_path):
    """Process with Qwen VL."""
    # Prompt for Qwen to generate structured markdown
    prompt = "You are a helpful assistant. Please extract the text and layout from this image and provide it in Markdown format."
    return call_ollama(QWEN_MODEL, prompt, image_path)

def save_output(content, output_dir, file_stem):
    """Save content to md and txt files."""
    if content is None:
        content = "Error: Extraction failed."
    
    # Save structured markdown
    with open(os.path.join(output_dir, "md", f"{file_stem}.md"), "w", encoding="utf-8") as f:
        f.write(content)
    
    # Save raw text (stripping markdown simple approach, or just same content if user accepts markdown as text representation)
    # The user asked for "txt, md". 
    # Usually txt means plain text without markdown formatting. 
    # For now I will save the same content to txt or try to strip rudimentary tags if needed.
    # But Qwen/Deepseek return markdown. Let's save the markdown content as .txt too or just raw.
    with open(os.path.join(output_dir, "txt", f"{file_stem}.txt"), "w", encoding="utf-8") as f:
        f.write(content)

def main():
    print("Starting Comparison Task...")
    
    # 1. Convert PDF
    image_files = pdf_to_png(PDF_PATH, os.path.join(OUTPUT_DIR, "images"))
    
    results = []
    
    for img_path in image_files:
        stem = Path(img_path).stem
        print(f"\nProcessing {stem}...")
        
        # DeepSeek
        deepseek_out_path = os.path.join(OUTPUT_DIR, "deepseek", "md", f"{stem}.md")
        if os.path.exists(deepseek_out_path):
             print(f"  DeepSeek output exists, skipping.")
             deepseek_result = "SKIPPED"
             deepseek_duration = 0
        else:
            start_time = time.time()
            deepseek_result = deepseek_process(img_path)
            deepseek_duration = time.time() - start_time
            save_output(deepseek_result, os.path.join(OUTPUT_DIR, "deepseek"), stem)
            print(f"  DeepSeek: {deepseek_duration:.2f}s")
        
        # Qwen
        qwen_out_path = os.path.join(OUTPUT_DIR, "qwen", "md", f"{stem}.md")
        if os.path.exists(qwen_out_path):
             print(f"  Qwen output exists, skipping.")
             qwen_result = "SKIPPED"
             qwen_duration = 0
        else:
            start_time = time.time()
            qwen_result = qwen_process(img_path)
            qwen_duration = time.time() - start_time
            save_output(qwen_result, os.path.join(OUTPUT_DIR, "qwen"), stem)
            print(f"  Qwen: {qwen_duration:.2f}s")
        
        results.append({
            "page": stem,
            "deepseek_time": deepseek_duration,
            "qwen_time": qwen_duration,
            "deepseek_len": len(deepseek_result) if deepseek_result else 0,
            "qwen_len": len(qwen_result) if qwen_result else 0
        })
        
        # Optional: Sleep to avoid overheating/overload if needed
        # time.sleep(1)

    # Report
    print("\n" + "="*40)
    print("Comparison Report")
    print("="*40)
    print(f"{'Page':<10} | {'DeepSeek (s)':<12} | {'Qwen (s)':<12} | {'DS Len':<8} | {'Qwen Len':<8}")
    print("-" * 60)
    
    total_ds_time = 0
    total_qwen_time = 0
    
    for r in results:
        print(f"{r['page']:<10} | {r['deepseek_time']:<12.2f} | {r['qwen_time']:<12.2f} | {r['deepseek_len']:<8} | {r['qwen_len']:<8}")
        total_ds_time += r['deepseek_time']
        total_qwen_time += r['qwen_time']
        
    print("-" * 60)
    print(f"Total Time | {total_ds_time:<12.2f} | {total_qwen_time:<12.2f}")
    
    report_path = os.path.join(OUTPUT_DIR, "comparison_report.json")
    with open(report_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nReport saved to {report_path}")

if __name__ == "__main__":
    main()
