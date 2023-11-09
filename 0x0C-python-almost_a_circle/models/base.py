#!/usr/bin/python3
'''models/base.py'''


class Base:
    """A base class for other classes in the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """The class constructor

        Args:
            id (int, optional): The id of the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
