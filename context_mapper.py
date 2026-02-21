import os

def generate_index(docs_dir="context_chunks"):
    if not os.path.exists(docs_dir):
        print(f"Directory {docs_dir} not found. Run md_chunker.py first.")
        return

    index_content = "# Project Documentation Index\n\n"
    index_content += "Upload only the specific file needed for the current task.\n\n"
    
    files = sorted([f for f in os.listdir(docs_dir) if f.endswith(".md")])
    for file in files:
        with open(os.path.join(docs_dir, file), 'r') as f:
            first_line = f.readline().strip().lstrip('#').strip()
            index_content += f"- **{file}**: {first_line}\n"
    
    with open("INDEX.md", "w") as f:
        f.write(index_content)
    print("INDEX.md generated successfully.")

if __name__ == "__main__":
    generate_index()
