import os

def replace_string_in_files(old_string, new_string, directory='.'):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                if old_string in content:
                    new_content = content.replace(old_string, new_string)
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Replaced in: {file_path}")
            except (UnicodeDecodeError, PermissionError, IsADirectoryError) as e:
                print(f"Skipped {file_path}: {e}")

# Example usage
old = "old_string_here"
new = "new_string_here"
replace_string_in_files(old, new)
