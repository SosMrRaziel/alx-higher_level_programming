#!/usr/bin/python3
''''from_json_string  a function that returns an object
(Python data structure) represented by a JSON string:'''


import json


def from_json_string(my_str):
    '''convert the JSON string to a Python object using json.loads()'''
    return json.loads(my_str)
