import os
import json
import glob

# Define paths
base_dir = os.getcwd()
webp_dir = os.path.join(base_dir, 'webp')
pages_json_path = os.path.join(base_dir, 'pages.json')

# 1. Rename files in webp directory
print("Renaming files in webp directory...")
renamed_count = 0
for filename in os.listdir(webp_dir):
    if '[' in filename or ']' in filename:
        new_filename = filename.replace('[', '').replace(']', '_')
        # Remove double underscores if any, just in case
        new_filename = new_filename.replace('__', '_')
        
        old_path = os.path.join(webp_dir, filename)
        new_path = os.path.join(webp_dir, new_filename)
        
        os.rename(old_path, new_path)
        renamed_count += 1
        print(f"Renamed: {filename} -> {new_filename}")

print(f"Total files renamed: {renamed_count}")

# 2. Update pages.json
print("\nUpdating pages.json...")
with open(pages_json_path, 'r', encoding='utf-8') as f:
    pages_data = json.load(f)

updated_count = 0
for page in pages_data:
    if 'file' in page:
        original_file = page['file']
        if '[' in original_file or ']' in original_file:
            new_file = original_file.replace('[', '').replace(']', '_').replace('__', '_')
            page['file'] = new_file
            updated_count += 1

with open(pages_json_path, 'w', encoding='utf-8') as f:
    json.dump(pages_data, f, ensure_ascii=False, indent=2)

print(f"Total pages.json entries updated: {updated_count}")

# 3. Create .nojekyll file
nojekyll_path = os.path.join(base_dir, '.nojekyll')
if not os.path.exists(nojekyll_path):
    with open(nojekyll_path, 'w') as f:
        pass
    print("\nCreated .nojekyll file.")
else:
    print("\n.nojekyll file already exists.")
