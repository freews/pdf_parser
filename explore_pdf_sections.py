
import pymupdf # fitz
import sys

pdf_path = "./source_doc/NVM-Express-Base-Specification-Revision-2p3.pdf"

try:
    doc = pymupdf.open(pdf_path)
    print(f"Opened PDF: {pdf_path}")
    print(f"Total Pages: {len(doc)}")

    # Method 1: TOC
    print("\n--- Method 1: Document Outline (TOC) ---")
    toc = doc.get_toc()
    if toc:
        print(f"Found {len(toc)} TOC entries.")
        print("Sample (first 10):")
        for t in toc[:10]:
            lvl, title, page = t
            print(f"Lvl: {lvl}, Page: {page}, Title: {title}")
            
        print("\nSample (around page 292):")
        for t in toc:
            # item[2] is page number (1-based)
            if 290 <= t[2] <= 300:
                 print(f"Lvl: {t[0]}, Page: {t[2]}, Title: {t[1]}")
    else:
        print("No TOC found.")

    # Method 2: Text Search for Headers (Feasibility)
    print("\n--- Method 2: Text Search on Page 292-294 ---")
    import re
    # Match headers like "5.2.12.1.20 Title"
    # Note: Text extraction varies. We look for lines starting with numbering.
    header_regex = re.compile(r'^(\d+(\.\d+)+)\s+(.+)$')
    
    for p_num in range(291, 294): # 0-indexed access for pages 292-294
        page = doc.load_page(p_num)
        text = page.get_text("text")
        valid_page_num = p_num + 1
        print(f"\n--- Page {valid_page_num} Analysis ---")
        
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if header_regex.match(line):
                print(f"[POSSIBLE HEADER] {line}")

except Exception as e:
    print(f"Error: {e}")
