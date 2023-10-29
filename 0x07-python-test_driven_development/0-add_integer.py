#!/usr/bin/python3
'''' add_integer: adding two number'''


def add_integer(a, b=98):
    '''
    Adds two integers.

        a (int or float): First number.
        b (int or float, optional): Second number. Defaults to 98.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
