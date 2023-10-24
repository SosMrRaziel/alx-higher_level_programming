#!/usr/bin/python3
'''cass square'''


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initialize the square with a given size"""
        try:
            self.__size = int(size)
        except ValueError:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
