'''Define a class Student'''


class Student:
    '''Initialize the instance attributes'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    '''Define a method to return a dictionary
    representation of the instance'''
    def to_json(self):
        return self.__dict__
