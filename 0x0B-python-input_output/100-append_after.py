#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Appends a line of text to a file,
    after each line containing a specific string."""
    # Open the file in read mode and store its contents in a list
    with open(filename, "r") as f:
        lines = f.readlines()

    # Create a new list to store the modified lines
    new_lines = []

    # Loop through each line in the original file
    for line in lines:
        # Add the line to the new list
        new_lines.append(line)
        # Check if the line contains the search string
        if search_string in line:
            # Add the new string to the new list,
            # followed by a newline character
            new_lines.append(new_string + "\n")

    # Open the file in write mode and overwrite its contents with the new list
    with open(filename, "w") as f:
        f.writelines(new_lines)
