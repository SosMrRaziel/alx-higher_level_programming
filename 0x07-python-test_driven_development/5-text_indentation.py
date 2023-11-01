#!/usr/bin/python3
'''text indentation function'''


def text_indentation(text):
    """Prints two new lines after
    characters: ., ? and :
    Args:
        text (str): string text
    Raises:
        TypeError: if `text` is not string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    string = ''
    i = 0
    while i < len(text):
        string += text[i]
        if text[i] in ['.', '?', ':']:
            string = string.strip()
            print(string + '\n')
            try:
                if text[i + 1] == ' ':
                    i += 1
            except IndexError:
                pass
            string = ''
        i += 1

    if len(string) > 0:
        print(string, end="")
