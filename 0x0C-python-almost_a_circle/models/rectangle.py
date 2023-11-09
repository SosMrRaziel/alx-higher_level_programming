#!/usr/bin/python3
'''In the file models/rectangle.py'''


from models.base import Base


class Rectangle(Base):
    """A class that represents a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        # Call the super class with id
        # Assign each argument width, height, x and y to the right attribute
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        # Validate what a developer is trying to assign to a variable
        if type(value) is not int:
            raise TypeError("width must be an integer")
        # If width is under or equals 0, raise the ValueError
        # exception with the message: width must be > 0
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        # Validate what a developer is trying to assign to a variable
        # If the input is not an integer, raise the TypeError
        # exception with the message: height must be an integer
        if type(value) is not int:
            raise TypeError("height must be an integer")
        # If height is under or equals 0, raise the ValueError
        # exception with the message: height must be > 0
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        # Validate what a developer is trying to assign to a variable
        # If the input is not an integer, raise the TypeError exception
        # with the message: x must be an integer
        if type(value) is not int:
            raise TypeError("x must be an integer")
        # If x is under 0, raise the ValueError exception
        # with the message: x must be >= 0
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        # Validate what a developer is trying to assign to a variable
        # If the input is not an integer, raise the TypeError
        # exception with the message: y must be an integer
        if type(value) is not int:
            raise TypeError("y must be an integer")
        # If y is under 0, raise the ValueError
        # exceptionwith the message: y must be >= 0

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
