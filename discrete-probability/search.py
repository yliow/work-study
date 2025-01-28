import os

def search_latex_files(search_string, directory):
    """
    Searches for LaTeX files in a specified directory that contain a given string.

    Args:
        search_string (str): The string to search for.
        directory (str): The directory to search in.

    Returns:
        list: A list of LaTeX files containing the search string.
    """
    matching_files = []

    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".tex"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if search_string in content:
                            matching_files.append(file_path)
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    return matching_files

if __name__ == "__main__":
    # Get user input
    search_string = input("Enter the string to search for: ").strip()
    directory = input("Enter the directory to search in: ").strip()

    # Search LaTeX files
    result = search_latex_files(search_string, directory)

    # Print results
    if result:
        print("\nFiles containing the string:")
        for file in result:
            print(file)
    else:
        print("\nNo LaTeX files containing the string were found.")
