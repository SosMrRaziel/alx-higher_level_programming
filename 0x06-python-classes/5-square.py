#!/usr/bin/python3
'''calc square'''


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initialize the square with a given size"""

        self.size = size

    @property
    def size(self):
        """Return the size attribute"""

        return self.__size

    @size.setter
    def size(self, value):
        """Set the size attribute"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the current square area"""

        return self.__size ** 2

    def my_print(self):
        """Print the square with '#' characters"""

        if self.__size == 0:
            print()
            return
        for s in range(self.__size):
            print("#" * self.__size)
