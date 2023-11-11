#!/usr/bin/python3
'''models/base.py'''
import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): A list of dictionaries

        Returns:
            str: The JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string

        Args:
            json_string (str): A string representing a list of dictionaries

        Returns:
            list: The list represented by json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

        Args:
            dictionary (dict): A dictionary of key-value pairs for attributes

        Returns:
            Base: An instance of the class with the attributes set
        """
        # Create a dummy instance with default values
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        # Update the dummy instance with the dictionary values
        dummy.update(**dictionary)
        # Return the updated instance
        return dummy