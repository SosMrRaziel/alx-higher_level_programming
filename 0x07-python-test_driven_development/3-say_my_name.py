#!/usr/bin/python3
'''say_my_name to print your full name'''


def say_my_name(first_name, last_name=""):
    '''say_my_name is a functiion that print your full name
    first_name is required and should be a string
    last_name is optional and should be a tring'''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
