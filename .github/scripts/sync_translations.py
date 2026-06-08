import os
import json
import re
import sys

KEYS_FILE = "_keys.json"
CROWDIN_SOURCE_FILE = "keys-crowdin.json"

def clean_keys_for_crowdin():
    if not os.path.exists(KEYS_FILE):
        print(f"Error: {KEYS_FILE} not found.")
        sys.exit(1)

    # Read the master file with comments
    with open(KEYS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Strip out all single-line comments (// ...) cleanly
    clean_content = re.sub(r'^(?:[^"\n]|"(?:[^"\\]|\\.)*")*?(//.*)$', '', content, flags=re.MULTILINE)
    
    # Parse to ensure it's valid syntax
    try:
        source_keys = json.loads(clean_content)
    except Exception as e:
        print(f"Error validating strict JSON syntax: {e}")
        sys.exit(1)
    
    # Save the comment-free version for Crowdin
    with open(CROWDIN_SOURCE_FILE, 'w', encoding='utf-8') as f:
        json.dump(source_keys, f, indent=2, ensure_ascii=False)
        f.write("\n")
        
    print(f"Successfully updated clean source file: {CROWDIN_SOURCE_FILE}")

if __name__ == "__main__":
    clean_keys_for_crowdin()
