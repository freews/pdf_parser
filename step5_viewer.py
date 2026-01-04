import json
import os

INPUT_JSON = "./out/section_content_with_summary.json"

def main():
    print("="*60)
    print("PDF SECTION SUMMARY VIEWER")
    print("="*60)
    
    if not os.path.exists(INPUT_JSON):
        print("No data found.")
        return

    with open(INPUT_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for section in data:
        print(f"[{section.get('section_id', '?')}] {section.get('title', 'No Title')}")
        print(f"Pages: {section.get('start_page')} - {section.get('end_page')}")
        print("-" * 30)
        print(f"SUMMARY: {section.get('summary', 'N/A')}")
        print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    main()
