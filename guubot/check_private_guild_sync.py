from __future__ import annotations

import os
import re
import sys

TARGET_STRING = ", guild=discord.Object(id=client.envir))"
COMMENT_STYLE = "#"

def escape_special_characters(target_string):
    """
    Escapes special characters in the target string to be safely used in regex.
    """

    # Check if the line contains the target string
    if TARGET_STRING in line:
        # Find the part of the line that includes the target string and comment it out
        # First, split the line at the target string, then append the `)` and comment style
        pre_comment = line.split(escaped_target_string)[0].rstrip()
        comment_part = line.split(escaped_target_string)[1]
        
        # Add the closing parenthesis before the comment and apply the comment style
        modified_line = f"{pre_comment}) {COMMENT_STYLE}{escaped_target_string}{comment_part}"
        return modified_line

    return line

def check_and_comment_file(file_path):
    """
    Reads the file, checks for the target string, and comments it out if necessary.
    """
    with open(file_path, "r") as file:
        lines = file.readlines()

    modified_lines = [comment_out_end_of_line(line) for line in lines]

    # Write back the modified content to the file
    with open(file_path, "w") as file:
        file.writelines(modified_lines)

def is_code_file(file_path):
    """
    Filter to only apply the check to code files (e.g., .py).
    """
    return file_path.endswith('.py')

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
    raise SystemExit(main())
