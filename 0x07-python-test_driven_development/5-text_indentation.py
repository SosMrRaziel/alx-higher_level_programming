#!/usr/bin/python3
"""
5-text_indentation.py
def text_indentation(text)
tests/5-text_indentation.txt
"""


def text_indentation(text):
    """
    Prints text with two newlines separating each line
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.strip(" ")
    sep = [".", "?", ":"]
    i = 0
    while i < len(text):
        if text[i] in sep:
            print("{}\n".format(text[i]))
            i += 1
            if i == len(text):
                return
            while text[i] is " " and i < len(text):
                i += 1
            continue
        print("{}".format(text[i]), end='')
        i += 1
        if i == len(text) and text[i - 1] in sep:
            print("\n")
