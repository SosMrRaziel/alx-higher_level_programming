#!/usr/bin/python3
'''define Rectangle class'''


class Rectangle:
    """A class that defines a rectangle by its width and height"""

    # Public class attribute that counts the number of instances
    number_of_instances = 0

    # Public class attribute that stores the symbol for string representation
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height"""
        self.width = width
        self.height = height
        # Increment the number of instances for each new instance
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """The width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        new_str = ""
        for i in range(self.__height - 1):
            new_str += str(self.print_symbol) * self.__width + "\n"
        new_str += str(self.print_symbol) * self.__width
        return new_str

    def __repr__(self):
        """Return a string representation of the rectangle
        to be able to recreate a new instance by using eval()"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        # Decrement the number of instances for each deleted instance
        Rectangle.number_of_instances -= 1
