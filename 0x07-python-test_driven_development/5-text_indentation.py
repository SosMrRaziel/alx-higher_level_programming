#!/usr/bin/python3
'''text indentation function'''


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be printed

    Raises:
        TypeError: If `text` is not a string

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i])
            print()
            if i < len(text) - 1 and text[i + 1] == ' ':
                i += 1
        else:
            print(text[i], end="")
        i += 1
