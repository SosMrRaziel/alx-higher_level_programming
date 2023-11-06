#!/usr/bin/python3
"""base_geometry"""


class BaseGeometry:
    """A class that defines basic geometrical shapes"""

    def area(self):
        """A method that raises an exception for unimplemented areas"""
        raise Exception("area() is not implemented")
