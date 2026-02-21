import sys

def estimate_tokens(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            # Heuristic: 1 token is approx 4 characters or 0.75 words
            word_count = len(text.split())
            token_est = int(word_count * 1.35)
            
            print(f"--- Token Report ---")
            print(f"File: {file_path}")
            print(f"Estimated Tokens: {token_est}")
            
            if token_est > 6000:
                print("Status: ❌ TOO LARGE. Use md_chunker.py.")
            else:
                print("Status: ✅ OPTIMIZED for Claude/Gemini.")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        estimate_tokens(sys.argv[1])
    else:
        print("Usage: python token_check.py <your_file.md>")
