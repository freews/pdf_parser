
import pymupdf
import json
import re
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

pdf_path = "./source_doc/NVM-Express-Base-Specification-Revision-2p3.pdf"
output_path = "./out/pdf_structure.json"

def extract_structure():
    """
    Extracts the Table of Contents (TOC) structure from the PDF file.
    
    This function performs the following steps:
    1. Opens the PDF using pymupdf (fitz).
    2. Retrieves the TOC.
    3. Iterates through the TOC entries to extract section ID, title, and page range.
    4. Filters out irrelevant sections (e.g., introductory pages, lowercase titles).
    5. Calculates the end page for each section based on the start of the next section.
    6. Saves the structured data to a JSON file.
    """
    try:
        # verify file exists
        if not os.path.exists(pdf_path):
            logger.error(f"PDF file not found at: {pdf_path}")
            return

        doc = pymupdf.open(pdf_path)
        toc = doc.get_toc() # Returns list of [lvl, title, page_num] where page_num is 1-based
        
        structure = []
        
        # Regex to extract Section ID from title (e.g., "5.2.12.1.19 NVMe-MI..." -> "5.2.12.1.19")
        # Also supports Annex IDs (e.g., "Annex A ...", "B.6.1 ...")
        id_pattern = re.compile(r'^((?:Annex\s+)?[A-Z\d][\w\.]*)\s+(.*)')
        
        # Manually add Cover section (Page 1)
        # This is often missed by standard TOC
        logger.info("Adding manual 'Cover' section.")
        structure.append({
            "section_order": 1,
            "level": 1,
            "section_id": "Cover",
            "title": "Cover",
            "start_page": 1,
            "end_page": 1,
            "page_count": 1
        })

        seen_ids = set()
        
        logger.info(f"Processing {len(toc)} TOC entries...")

        for i, entry in enumerate(toc):
            lvl, title, page_num = entry
            
            # --- FILTERING ---
            
            # 1. Skip Front Matter Pages (2-24)
            # Adjust this range as needed for specific documents
            if 2 <= page_num <= 24:
                continue

            # 2. Parse Section ID and Title
            match = id_pattern.match(title)
            if match:
                sec_id = match.group(1).rstrip('.')
                sec_title = match.group(2)
            else:
                # Sections without explicit ID (e.g., Introduction)
                # Or titles that didn't match the regex pattern
                sec_id = "" 
                sec_title = title

            # 3. Skip Lowercase Titles
            # These are often garbage entires or minor definitions not worth separate sections
            if sec_title and sec_title[0].islower():
                continue

            # 4. Skip Duplicates
            if sec_id and sec_id in seen_ids:
                logger.warning(f"Skipping duplicate ID: {sec_id}")
                continue
            
            if sec_id:
                seen_ids.add(sec_id)

            # --- PAGE RANGE CALCULATION ---
            
            # Calculate end page based on the start page of the NEXT TOC entry
            # Note: The logic handles non-contiguous TOC entries (e.g. if we skipped some above)
            # by using the raw index `i`. However, strictly speaking, validity should be 
            # checked against the document length.
            
            if i < len(toc) - 1:
                next_start_page = toc[i+1][2]
                # The current section ends one page before the section starts
                current_end_inclusive = next_start_page - 1
            else:
                # Last section goes to the end of the document
                current_end_inclusive = len(doc)
            
            # Clamp: Ensure end page is not before start page 
            # (Possible if multiple TOC entries point to the same page)
            if current_end_inclusive < page_num:
                current_end_inclusive = page_num

            # Append to structure list
            structure.append({
                "section_order": len(structure) + 1,
                "level": lvl,
                "section_id": sec_id,
                "title": sec_title,
                "start_page": page_num,
                "end_page": current_end_inclusive,
                "page_count": current_end_inclusive - page_num + 1
            })

        # Save to JSON
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(structure, f, indent=4)
            
        logger.info(f"Structure extracted to {output_path}. Total sections: {len(structure)}")
        
        # Log a few sample sections for verification
        if structure:
            logger.info(f"First Section: {structure[0]}")
            logger.info(f"Last Section: {structure[-1]}")

    except Exception as e:
        logger.error(f"Error extracting structure: {e}")

if __name__ == "__main__":
    extract_structure()
