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
        # If the input is not an integer, raise the TypeError exception with the message: width must be an integer
        if type(value) is not int:
            raise TypeError("width must be an integer")
        # If width is under or equals 0, raise the ValueError exception with the message: width must be > 0
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of the Square instance"""
        # Use the format method to insert the values of the attributes in the string
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Public method that assigns arguments to attributes"""
        # If *args exists and is not empty, assign each argument to the right attribute
        if args:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        # If **kwargs exists and is not empty, assign each key/value pair to the right attribute
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)