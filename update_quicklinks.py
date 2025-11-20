import json
import os

file_path = r'c:\Users\김건우\Desktop\VS\Catalog\quicklinks.json'

def update_page_numbers():
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        def recursive_update(items):
            for item in items:
                if 'page' in item and isinstance(item['page'], int):
                    item['page'] += 2
                
                if 'children' in item and isinstance(item['children'], list):
                    recursive_update(item['children'])

        recursive_update(data)

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print("Successfully updated page numbers.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    update_page_numbers()
