#!/usr/bin/python3
"""BaseGeometry"""


class BaseGeometry:
    """A class that represents a base geometry"""

    def area(self):
        """A method that raises an exception for unimplemented area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A method that validates an integer value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
