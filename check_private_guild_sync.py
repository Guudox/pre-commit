import os
import sys

# Define the target string and comment style (e.g., '#' for Python, '//' for JavaScript)
TARGET_STRING = ", guild=discord.Object(id=client.envir))"
COMMENT_STYLE = "#"

def comment_out_line(line):
    """
    Comments out the line if the target string is found and the line is not already commented.
    """
    stripped_line = line.strip()
    
    # Check if the line contains the target string and is not already commented
    if TARGET_STRING in stripped_line and not stripped_line.startswith(COMMENT_STYLE):
        return f"{COMMENT_STYLE} {line}"
    
    return line

def check_and_comment_file(file_path):
    """
    Reads the file, checks for the target string, and comments it out if necessary.
    """
    with open(file_path, "r") as file:
        lines = file.readlines()

    modified_lines = [comment_out_line(line) for line in lines]

    # Write back the modified content to the file
    with open(file_path, "w") as file:
        file.writelines(modified_lines)

def is_code_file(file_path):
    """
    Filter to only apply the check to code files (e.g., .py, .js, etc.).
    Modify the extensions as needed.
    """
    return file_path.endswith(('.py'))

def main():
    """
    Main function to iterate over staged files and apply the check.
    """
    # Get the list of staged files
    staged_files = os.popen('git diff --cached --name-only').read().splitlines()

    # Apply the check to each staged file
    for file_path in staged_files:
        if is_code_file(file_path):
            print(f"Checking file: {file_path}")
            check_and_comment_file(file_path)

if __name__ == "__main__":
    main()
