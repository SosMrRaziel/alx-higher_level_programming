#!/usr/bin/python3
'''append_write a function that appends a string at the end of
a text file (UTF8) and returns the number of characters added'''


def append_write(filename="", text=""):
    '''open the file in append mode with UTF-8 encoding'''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
