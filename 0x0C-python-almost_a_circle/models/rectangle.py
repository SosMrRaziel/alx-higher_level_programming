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
        # If the input is not an integer, raise the TypeError
        if type(value) is not int:
            raise TypeError("width must be an integer")
        # If width is under or equals 0, raise the ValueError
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        # If height is under or equals 0, raise the ValueError
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
        # If the input is not an integer, raise the TypeError
        if type(value) is not int:
            raise TypeError("x must be an integer")
        # If x is under 0, raise the ValueError
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
        if type(value) is not int:
            raise TypeError("y must be an integer")
        # If y is under 0, raise the ValueError
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Public method that returns the area
        value of the Rectangle instance"""
        # The area of a rectangle is the product of its width and height
        return self.__width * self.__height

    def display(self):
        """Public method that prints in stdout
        the Rectangle instance with the character #"""
        # To print a margin above the rectangle,
        # you need to print a new line for each y unit
        print("\n" * self.y, end="")
        # To print a rectangle, you need to print a row of
        # characters for each height unit
        # and repeat that for each width unit
        # You can use a nested loop to achieve this
        for i in range(self.height):
            # To print a margin on the left of the rectangle,
            # you need to print a space for each x unit
            print(" " * self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print()  # To start a new line after each row

    def __str__(self):
        """String representation of the Rectangle instance"""
        # Use the format method to insert
        # the values of the attributes in the string
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def to_dictionary(self):
        """Public method that returns the dictionary representation of a Rectangle"""
        # Create an empty dictionary
        rectangle_dict = {}
        # Assign the values of the attributes to the keys in the dictionary
        rectangle_dict["id"] = self.id
        rectangle_dict["width"] = self.width
        rectangle_dict["height"] = self.height
        rectangle_dict["x"] = self.x
        rectangle_dict["y"] = self.y
        # Return the dictionary
        return rectangle_dict