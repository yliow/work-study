import os

def update_latex_files(directory, to_change, change_to):
    """
    Recursively goes through all .tex files in the given directory and replaces
    occurrences of "exercises/" with "exercises/discrete-probability/".

    Args:
        directory (str): Path to the root directory to search.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".tex"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Replace the target string
                updated_content = content.replace(to_change, change_to)

                # Write the updated content back to the file if changes were made
                if content != updated_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    print(f"Updated: {file_path}")

if __name__ == "__main__":
    # Specify the directory containing your LaTeX files
    latex_dir = input("Enter the path to your LaTeX files directory: ")
    to_change = "exercises/discrete-probability/"
    change_to = ""
    if os.path.isdir(latex_dir):
        update_latex_files(latex_dir, to_change, change_to)
    else:
        print("Invalid directory. Please check the path and try again.")
