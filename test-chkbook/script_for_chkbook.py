import os
import shutil
import subprocess

# Path to this script
script_path = os.path.abspath("chkbook.py")
script_name = os.path.basename(script_path)
base_dir = os.path.dirname(script_path)

# Find all sibling directories (excluding hidden ones and __pycache__)
subdirs = [
    d for d in os.listdir(base_dir)
    if os.path.isdir(os.path.join(base_dir, d)) and not d.startswith('.') and d != '__pycache__'
]

for d in subdirs:
    target_dir = os.path.join(base_dir, d)
    target_script_path = os.path.join(target_dir, script_name)

    # Copy this script to the target directory
    shutil.copy2(script_path, target_script_path)
    print(f"Copied to {target_script_path}")

    # Run the copied script in that directory
    subprocess.run(['python', script_name], cwd=target_dir)
