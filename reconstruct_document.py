import json
import os
import base64
import re
import markdown
from pathlib import Path

# Configuration
INPUT_JSON_PATH = "./out/output_json/section_info.json"
OUTPUT_HTML_PATH = "./out/restored_document.html"
OUTPUT_IMAGE_FOLDER = "./out/restored_images"

CSS_STYLE = """
<style>
    body { 
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; 
        line-height: 1.6; 
        color: #333; 
        max-width: 900px; 
        margin: 0 auto; 
        padding: 40px; 
        background-color: #f9f9f9;
    }
    .container {
        background-color: #fff;
        padding: 50px;
        box-shadow: 0 0 15px rgba(0,0,0,0.05);
        border-radius: 8px;
    }
    h1, h2, h3, h4, h5, h6 { color: #2c3e50; margin-top: 1.5em; margin-bottom: 0.5em; }
    h1 { border-bottom: 2px solid #eee; padding-bottom: 10px; }
    h2 { border-bottom: 1px solid #eee; padding-bottom: 5px; }
    
    table { 
        border-collapse: collapse; 
        width: 100%; 
        margin: 20px 0; 
        font-size: 0.95em;
    }
    th, td { 
        border: 1px solid #e1e4e8; 
        padding: 10px 15px; 
        text-align: left; 
    }
    th { 
        background-color: #f6f8fa; 
        font-weight: 600; 
    }
    tr:nth-child(even) { background-color: #fcfcfc; }
    
    img { 
        max-width: 100%; 
        height: auto; 
        display: block; 
        margin: 20px auto; 
        border: 1px solid #ddd;
        border-radius: 4px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .figure-caption {
        text-align: center;
        font-style: italic;
        color: #666;
        margin-bottom: 20px;
        font-size: 0.9em;
    }
    code {
        background-color: #f6f8fa;
        padding: 2px 5px;
        border-radius: 3px;
        font-family: Consolas, monospace;
    }
    pre {
        background-color: #f6f8fa;
        padding: 15px;
        border-radius: 5px;
        overflow-x: auto;
    }
    hr { border: 0; border-top: 1px solid #eee; margin: 40px 0; }
</style>
"""

def setup_directories():
    os.makedirs(OUTPUT_IMAGE_FOLDER, exist_ok=True)
    os.makedirs(os.path.dirname(OUTPUT_HTML_PATH), exist_ok=True)

def decode_and_save_image(base64_string, image_name):
    """Decodes base64 string and saves as PNG."""
    try:
        # Clean image name to be filename safe
        safe_name = image_name.replace(" ", "_").replace(":", "").replace("/", "_")
        filename = f"{safe_name}.png"
        filepath = os.path.join(OUTPUT_IMAGE_FOLDER, filename)
        
        with open(filepath, "wb") as f:
            f.write(base64.b64decode(base64_string))
        
        return filename
    except Exception as e:
        print(f"❌ Error saving image {image_name}: {e}")
        return None

def process_section(section, full_html_parts):
    # 1. Prepare Header
    depth = section.get('section_depth', 1)
    title = section.get('section_title', '')
    s_id = section.get('section_ID', '')
    content = section.get('section_content', '')
    
    # Header Construction
    if s_id.lower() == 'cover':
         header_md = f"# {title}"
    else:
         header_md = f"{'#' * depth} {s_id} {title}"
    
    # Check for duplicate header in content
    should_add_header = True
    if content and content.strip():
        first_line = content.strip().split('\n')[0]
        # Check looser match
        if s_id in first_line and title in first_line:
             should_add_header = False
        # Check exact match
        if header_md.replace('#', '').strip() == first_line.replace('#', '').strip():
            should_add_header = False

    if should_add_header:
        # Convert header to HTML
        header_html = markdown.markdown(header_md)
        full_html_parts.append(header_html)

    # 2. Process Content (Markdown -> HTML)
    # Be careful with placeholders like <!-- Figure ... -->
    # We can pre-process them or let markdown handle them (comments are usually hidden).
    # We want to replace them with images if possible.
    
    # Decode images first to get filenames
    images = section.get('section_image', [])
    image_names = section.get('section_image_name_list', [])
    image_map = {} # Name -> Filename
    
    if images:
        for img_data, img_name in zip(images, image_names):
            filename = decode_and_save_image(img_data, img_name)
            if filename:
                image_map[img_name] = filename

    # Replace placeholders in content with Markdown Image syntax BEFORE conversion
    # Placeholder format: <!-- Figure [Name], coordinate:... -->
    # Regex to find these
    def replace_image_placeholder(match):
        full_tag = match.group(0) # The comment
        # We need to extract the name. 
        # The regex in parser was: r'<!-- (Figure|Embeded_Image) (.*?), coordinate:\((.*?)\) -->'
        # Let's try to find keys from image_map that match the tag content
        
        for name, filename in image_map.items():
            # Check if this name is in the tag
            # It's heuristic but usually robust if names are "Figure 1" etc.
            if name in full_tag:
                rel_path = f"restored_images/{filename}"
                # Return standard Markdown image
                return f"\n![{name}]({rel_path})\n*{name}*\n"
        
        return full_tag # No match found, keep as comment

    if content:
        # Do substitution
        content = re.sub(r'<!--\s*(Figure|Embeded_Image).*?-->', replace_image_placeholder, content)
        
        # Convert to HTML
        # Enable 'tables' extension
        content_html = markdown.markdown(content, extensions=['tables', 'fenced_code'])
        full_html_parts.append(content_html)

    # 3. Process Tables
    # section_table is list of list of strings (rows)
    tables = section.get('section_table', [])
    if tables:
        for table_rows in tables:
            # Join rows to make a markdown table block
            table_md = "\n".join([row.strip() for row in table_rows])
            # Convert to HTML
            table_html = markdown.markdown(table_md, extensions=['tables'])
            full_html_parts.append(table_html)
            
    # 4. Append orphan images (extracted but not found in text placeholders)
    # This might duplicate if placeholder logic worked perfectly, but safer ensures they show.
    # To avoid duplicate, we could track 'used' images. but placeholders are comments.
    # Let's assume if we replaced placeholder, we are good.
    # But if content didn't have placeholder (maybe stripped?), we need to check.
    # Simple check: is filename in content_html?
    for name, filename in image_map.items():
        rel_path = f"restored_images/{filename}"
        if rel_path not in (full_html_parts[-1] if full_html_parts else ""):
             # Append explicitly
             full_html_parts.append(f'<div class="figure"><img src="{rel_path}" alt="{name}"><div class="figure-caption">{name}</div></div>')

    full_html_parts.append("<hr>")

def reconstruct_document():
    print("🔄 Loading JSON data...")
    if not os.path.exists(INPUT_JSON_PATH):
        print(f"❌ Input file not found: {INPUT_JSON_PATH}")
        return

    with open(INPUT_JSON_PATH, 'r', encoding='utf-8') as f:
        sections = json.load(f)

    print(f"📄 Reconstructing document with {len(sections)} sections...")
    
    full_html_parts = []
    
    # HTML Header
    full_html_parts.append(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Restored Document</title>
        {CSS_STYLE}
    </head>
    <body>
    <div class="container">
    """)
    
    for section in sections:
        process_section(section, full_html_parts)
    
    # HTML Footer
    full_html_parts.append("""
    </div>
    </body>
    </html>
    """)

    print(f"💾 Saving to {OUTPUT_HTML_PATH}...")
    with open(OUTPUT_HTML_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(full_html_parts))
    
    print("✅ restoration Complete!")

if __name__ == "__main__":
    setup_directories()
    reconstruct_document()
