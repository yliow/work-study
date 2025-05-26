import os
import re

# Function to update LaTeX input commands
def update_latex_inputs(directory, prefix):
    """
    Updates all LaTeX files in the given directory by replacing 'input{b' with 'input{sb'.

    Parameters:
        directory (str): Path to the directory containing .tex files.
        prefix (str): The string to prepend to 'b' in the 'input' command.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".tex"):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Replace 'input{b' with 'input{sb'
                updated_content = re.sub(r"\\input\{([^}]+)\}", lambda m: f"\\input{{{prefix}{m.group(1)}}}", content)

                # Write changes back to the file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)

if __name__ == "__main__":
    # Directory containing LaTeX files
    directory_path = input("Enter the path to the directory containing .tex files: ")
    
    # Prefix to prepend to 'b' (e.g., "stdout/")
    prefix = input("Enter the prefix to prepend (e.g., 'stdout/'): ")

    update_latex_inputs(directory_path, prefix)
    print("Update complete!")
