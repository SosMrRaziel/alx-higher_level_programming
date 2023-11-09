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
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        # Validate what a developer is trying to assign to a variable
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        # Validate what a developer is trying to assign to a variable
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        # Validate what a developer is trying to assign to a variable
        self.__y = value
