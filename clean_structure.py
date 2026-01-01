import json
import os
import shutil

PDF_STRUCTURE_PATH = 'out/pdf_structure.json'
BACKUP_PATH = 'out/pdf_structure.json.bak'

def clean_structure():
    if not os.path.exists(PDF_STRUCTURE_PATH):
        print(f"Error: {PDF_STRUCTURE_PATH} not found.")
        return

    # Backup original
    shutil.copy(PDF_STRUCTURE_PATH, BACKUP_PATH)
    print(f"Backed up original to {BACKUP_PATH}")

    with open(PDF_STRUCTURE_PATH, 'r', encoding='utf-8') as f:
        structure = json.load(f)

    cleaned_structure = []
    seen_ids = set()
    
    removed_count = 0

    # Regex for patching IDs from title (e.g. "B.6.1 ...", "Annex C ...")
    import re
    id_patch_pattern = re.compile(r'^((?:Annex\s+)?[A-Z\d][\w\.]*)\s+(.*)')

    for section in structure:
        sec_id = section.get('section_id', '').strip()
        title = section.get('title', '').strip()
        
        # Rule: Patch missing ID if possible
        if not sec_id and title:
            match = id_patch_pattern.match(title)
            if match:
                sec_id = match.group(1).rstrip('.')
                print(f"Patched missing ID: '{sec_id}' from title '{title}'")
                section['section_id'] = sec_id
                # Update title to remove the ID part if we want to be consistent,
                # but let's just update the ID for now.
                # Actually, looking at previous extraction, title usually keeps the full text? 
                # Let's check the extraction script logic. 
                # Original extraction separates ID and Title.
                # "5.2.12.1.19 NVMe-MI..." -> ID="5.2.12.1.19", Title="NVMe-MI..."
                # So we should probably update title too.
                section['title'] = match.group(2)
        
        # Rule 1: Keep "Cover"
        if sec_id == "Cover":
            cleaned_structure.append(section)
            seen_ids.add(sec_id)
            continue

        # Rule 2: Skip empty IDs (unless it's allowed, but usually extraction should have ID)
        # Some intro sections might NOT have IDs, so we be careful. 
        # If the user says "duplicates", they imply IDs exist.
        # Let's assume empty ID is fine if title is valid, but "duplicates" refers to non-empty.
        
        # Rule 3: Check for duplicates
        if sec_id and sec_id in seen_ids:
            print(f"Removing duplicate ID: {sec_id} (Title: {title})")
            removed_count += 1
            continue
        
        # Rule 4: Check for lowercase title start (heuristic for garbage)
        # Ensure title is not empty before checking
        if title and title[0].islower():
            print(f"Removing lowercase title: {title} (ID: {sec_id})")
            removed_count += 1
            continue
            
        if sec_id:
            seen_ids.add(sec_id)
        
        cleaned_structure.append(section)

    with open(PDF_STRUCTURE_PATH, 'w', encoding='utf-8') as f:
        json.dump(cleaned_structure, f, indent=4)

    print(f"Cleaned structure saved to {PDF_STRUCTURE_PATH}")
    print(f"Removed {removed_count} sections.")
    print(f"Total remaining sections: {len(cleaned_structure)}")

if __name__ == "__main__":
    clean_structure()
