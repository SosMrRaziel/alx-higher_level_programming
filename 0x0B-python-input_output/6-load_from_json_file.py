#!/usr/bin/python3
'''load_from_json_file a function that creates
an Object from a “JSON file”'''


import json


def load_from_json_file(filename):
    '''open the file in read mode'''
    with open(filename, "r") as f:
        # load the JSON string and convert it to a Python object
        obj = json.load(f)
        return obj
