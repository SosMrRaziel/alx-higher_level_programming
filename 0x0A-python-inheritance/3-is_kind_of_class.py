#!/usr/bin/python3
'''is_kind_of_class'''


def is_kind_of_class(obj, a_class):
    '''Use the built-in isinstance function to check if obj
    is an instance of a_class or its subclasses'''
    return isinstance(obj, a_class)
