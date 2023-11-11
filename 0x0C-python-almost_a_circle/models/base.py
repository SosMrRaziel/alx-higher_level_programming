#!/usr/bin/python3
'''models/base.py'''

import json   # Import the json module
import os  # Import the os module


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
            return "[]"  # Return an empty string if list_dictionaries is None
        else:
            # Return the JSON string using json.dumps
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): A list of instances who inherits of Base
        """
        # The filename must be <Class name>.json
        filename = cls.__name__ + ".json"
        # An empty list to store the dictionaries of each object
        list_dicts = []
        if list_objs is not None:  # If list_objs is not None
            # For each object in list_objs
            for obj in list_objs:
                # Append the dictionary of the object to list_dicts
                list_dicts.append(obj.to_dictionary())
        with open(filename, "w") as f:  # Open the file in write mode
            # Write the JSON string of list_dicts to the file
            f.write(cls.to_json_string(list_dicts))

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
            # Return the list represented by json_string using json.loads
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        Args:
            dictionary (dict): A dictionary of attributes and values
        Returns:
            Base: An instance of Base or its subclasses
        """
        if cls.__name__ == "Rectangle":  # If the class is Rectangle
            # Create a dummy instance with width and height set to 1
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":  # If the class is Square
            dummy = cls(1)  # Create a dummy instance with size set to 1
        else:
            dummy = cls()  # Create a dummy instance with no arguments
        # Update the dummy instance with the dictionary values
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances

        Returns:
            list: A list of instances of Base or its subclasses
        """
        # The filename must be <Class name>.json
        filename = cls.__name__ + ".json"
        list_instances = []  # An empty list to store the instances
        if os.path.exists(filename):  # If the file exists
            with open(filename, "r") as f:  # Open the file in read mode
                # Read and convert the JSON string to a list of dictionaries
                list_dicts = cls.from_json_string(f.read())
            for dict in list_dicts:  # For each dictionary in the list
                # Create an instance with the dictionary values
                list_instances.append(cls.create(**dict))
        return list_instances
