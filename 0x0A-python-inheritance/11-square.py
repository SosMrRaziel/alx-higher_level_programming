#!/usr/bin/python3
"""Module for Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A subclass of Rectangle that represents a square"""

    def __init__(self, size):
        """Initialize a new Square instance

        Args:
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns a string representation of the Square instance"""
        return "[Square] {}/{}".format(self.__size, self.__size)
