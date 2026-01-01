
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
        tables = target_section.get("section_table_list", [])
        content_tables = target_section.get("section_table", [])
        
        print(f"Section {target_id} Detected Tables (names): {tables}")
        print(f"Section {target_id} Content Tables count: {len(content_tables)}")
        
        failed = False
        if not content_tables:
             print("FAIL: No table content found.")
             failed = True
        else:
             for idx, tbl in enumerate(content_tables):
                 if isinstance(tbl, list):
                     print(f"Table {idx} is a list with {len(tbl)} rows. PASS")
                 else:
                     print(f"Table {idx} is NOT a list (type: {type(tbl)}). FAIL")
                     failed = True
        
        if not failed:
            print("SUCCESS: Table structure verified.")
        else:
            print("VERIFICATION FAILED")

except Exception as e:
    print(f"Error reading or parsing json: {e}")
