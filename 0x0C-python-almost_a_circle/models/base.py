#!/usr/bin/python3
'''models/base.py'''

import json   # Import the json module
import os  # Import the os module
import csv


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

        filename = cls.__name__ + ".json"

        list_dicts = []
        if list_objs is not None:

            for obj in list_objs:

                list_dicts.append(obj.to_dictionary())
        with open(filename, "w") as f:

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

            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        Args:
            dictionary (dict): A dictionary of attributes and values
        Returns:
            Base: An instance of Base or its subclasses
        """
        if cls.__name__ == "Rectangle":

            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances
        Returns:
            list: A list of instances of Base or its subclasses
        """

        filename = cls.__name__ + ".json"
        list_instances = []
        if os.path.exists(filename):
            with open(filename, "r") as f:
                list_dicts = cls.from_json_string(f.read())
            for dict in list_dicts:

                list_instances.append(cls.create(**dict))
        return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV string representation of list_objs to a file

        Args:
            list_objs (list): A list of instances who inherits of Base
        """

        filename = cls.__name__ + ".csv"

        if list_objs is not None:

            with open(filename, "w", newline="") as f:
                writer = csv.writer(f)
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        # Write the id, width, height, x, y of the rectangle
                        writer.writerow(
                            [obj.id, obj.width, obj.height, obj.x, obj.y])
                    elif cls.__name__ == "Square":
                        # Write the id, size, x, y of the square
                        writer.writerow(
                            [obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances from a CSV file
        Returns:
            list: A list of instances of Base or its subclasses
        """
        filename = cls.__name__ + ".csv"
        list_instances = []
        if os.path.exists(filename):
            with open(filename, "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        # Create a dictionary of attributes for the rectangle
                        dict = {"id": int(row[0]),
                                "width": int(row[1]),
                                "height": int(row[2]),
                                "x": int(row[3]),
                                "y": int(row[4])}

                    elif cls.__name__ == "Square":
                        # Create a dictionary of attributes for the square
                        dict = {"id": int(row[0]),
                                "size": int(row[1]),
                                "x": int(row[2]),
                                "y": int(row[3])}

                    # Create an instance using dictionary & append to the list
                    list_instances.append(cls.create(**dict))
        return list_instances
