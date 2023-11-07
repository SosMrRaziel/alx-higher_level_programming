#!/usr/bin/python3
'''write_file a function that writes a string to a text file (UTF8)
and returns the number of characters written'''


def write_file(filename="", text=""):
    '''Use the with statement to open the file in write mode'''
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
