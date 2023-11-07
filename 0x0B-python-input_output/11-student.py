#!/usr/bin/python3
'''Define a class Student'''


class Student:
    """A class that represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize the student with first name, last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the student"""
        if attrs is None:
            # Return all attributes
            return self.__dict__
        else:
            # Return only the specified attributes
            return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """Replace all attributes of the student instance"""
        for k, v in json.items():
            setattr(self, k, v)
