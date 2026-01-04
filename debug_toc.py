
import pymupdf
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

pdf_path = "./source_doc/NVM-Express-Base-Specification-Revision-2p3.pdf"

def debug_toc():
    doc = pymupdf.open(pdf_path)
    toc = doc.get_toc()
    
    # We suspect sections around 1.7 (Page 39)
    # Let's print all TOC entries that are on pages 38-42
    
    print("Raw TOC entries for pages 30-50:")
    for entry in toc:
        lvl, title, page = entry
        if 30 <= page <= 50:
            print(f"Lvl: {lvl}, Page: {page}, Title: {title}")

if __name__ == "__main__":
    debug_toc()
