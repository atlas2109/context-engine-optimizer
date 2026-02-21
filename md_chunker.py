import os
import re

def split_markdown(file_path, output_dir="context_chunks"):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Splits file by # or ## headers
    sections = re.split(r'\n(?=#+ )', content)
    os.makedirs(output_dir, exist_ok=True)

    for i, section in enumerate(sections):
        header_match = re.search(r'#+ (.*)', section)
        safe_title = re.sub(r'[^\w\s-]', '', header_match.group(1)).strip().replace(" ", "_") if header_match else f"section_{i}"
        filename = f"{output_dir}/{i:02d}_{safe_title}.md"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(section.strip())
            
    print(f"Successfully split into {len(sections)} chunks in '{output_dir}/'")

if __name__ == "__main__":
    split_markdown("roadmap.md") # Change this to your filename
