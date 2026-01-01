
import json
import os

json_path = "./out/output_json/section_info.json"

try:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    target_id = "5.2.12.1.19"
    target_section = None
    for sec in data:
        if sec.get("section_ID") == target_id:
            target_section = sec
            break
            
    if not target_section:
        print(f"FAIL: Section {target_id} not found.")
    else:
        images = target_section.get("section_image_name_list", [])
        tables = target_section.get("section_table_list", [])
        
        print(f"Section {target_id} Images: {images}")
        print(f"Section {target_id} Tables: {tables}")
        
        # Verification Logic
        failed = False
        if "Figure 268" in images:
            print("FAIL: Figure 268 found in image list (should be ignored/moved).")
            failed = True
        else:
            print("PASS: Figure 268 NOT in image list.")
            
        if "Figure 269" in images:
            print("FAIL: Figure 269 found in image list (should be ignored/moved).")
            failed = True
        else:
            print("PASS: Figure 269 NOT in image list.")
            
        if "Figure 268" in tables:
            print("PASS: Figure 268 correctly detected as Table.")
        else:
            print("FAIL: Figure 268 NOT found in table list.")
            failed = True
            
        if "Figure 269" in tables:
            print("PASS: Figure 269 correctly detected as Table.")
        else:
            print("FAIL: Figure 269 NOT found in table list.")
            failed = True

        if not failed:
            print("SUCCESS: Table detection fix verified.")
        else:
            print("VERIFICATION FAILED")

except Exception as e:
    print(f"Error reading or parsing json: {e}")
