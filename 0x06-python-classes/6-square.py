#!/usr/bin/python3
'''calc square'''


class Square:
    """A class that represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a given size and position"""

        # Set the size attribute using the setter
        self.size = size

        # Set the position attribute using the setter
        self.position = position

    @property
    def size(self):
        """Return the size attribute"""

        # Return the private attribute
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size attribute"""

        # Check if value is an integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        # Check if value is positive
        if value < 0:
            raise ValueError("size must be >= 0")

        # Set the private attribute
        self.__size = value

    @property
    def position(self):
        """Return the position attribute"""

        # Return the private attribute
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position attribute"""

        # Check if value is a tuple of 2 positive integers
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        # Set the private attribute
        self.__position = value

    def area(self):
        """Return the current square area"""

        # Calculate the area as size squared
        return self.__size ** 2

    def my_print(self):
        """Print the square with '#' characters and position"""

        # Print an empty line if size is 0
        if self.__size == 0:
            print()
            return

        # Print the square using '#' characters and position
        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
