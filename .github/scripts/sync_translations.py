import os
import json
import re
import sys

# File Paths based on your repo structure
MANIFEST_FILE = "_manifest.json"
KEYS_FILE = "_keys.json"

def json_with_comments_to_dict(filepath):
    """Reads a JSON file that contains JS-style inline comments."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Remove single-line comments (// ...) but preserve strings containing URLs
    # This handles comments safely without breaking lines that have "https://"
    clean_content = re.sub(r'^(?:[^"\n]|"(?:[^"\\]|\\.)*")*?(//.*)$', '', content, flags=re.MULTILINE)
    return json.loads(clean_content)

def sync_translations():
    if not os.path.exists(MANIFEST_FILE) or not os.path.exists(KEYS_FILE):
        print("Missing _manifest.json or _keys.json in the root directory.")
        sys.exit(1)

    # Load source of truth
    try:
        source_keys = json_with_comments_to_dict(KEYS_FILE)
    except Exception as e:
        print(f"Error parsing _keys.json: {e}")
        sys.exit(1)

    # Load target languages from manifest
    with open(MANIFEST_FILE, 'r', encoding='utf-8') as f:
        manifest_data = json.load(f)
    
    languages = manifest_data.get("languages", [])

    for lang in languages:
        tag = lang.get("tag")
        if tag == "en": 
            continue # Skip English source file comparison if it exists as en.json
            
        filename = f"{tag}.json"
        
        # If the file doesn't exist yet, we initialize it empty
        if not os.path.exists(filename):
            print(f"File {filename} missing. Creating new language file.")
            target_data = {}
        else:
            with open(filename, 'r', encoding='utf-8') as f:
                try:
                    target_data = json.load(f)
                except json.JSONDecodeError:
                    print(f"Warning: {filename} was corrupt or empty. Resetting.")
                    target_data = {}

        updated = False
        
        # Check every key in source_keys
        for key, value in source_keys.items():
            if key not in target_data:
                target_data[key] = value  # Append the English string as fallback
                print(f"[{filename}] Added missing placeholder for key: {key}")
                updated = True

        # Write back to file if changes were made
        if updated:
            with open(filename, 'w', encoding='utf-8') as f:
                # keeps formatting clean, avoids escaping non-ASCII (for cyrillic, accents, etc.)
                json.dump(target_data, f, indent=2, ensure_ascii=False)
                # Add a trailing newline to keep git diffs happy
                f.write("\n")

if __name__ == "__main__":
    sync_translations()
