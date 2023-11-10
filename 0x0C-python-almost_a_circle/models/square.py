#!/usr/bin/python3
'''In the file models/square.py'''

from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        # Validate what a developer is trying to assign to a variable
        # If the input is not an integer, raise the TypeError
        if type(value) is not int:
            raise TypeError("width must be an integer")
        # If width is under or equals 0, raise the ValueError
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of the Square instance"""
        # Use the format method to insert the values of the attributes in the string
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)