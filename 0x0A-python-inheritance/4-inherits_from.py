#!/usr/bin/python3
'''inherits_from'''


def inherits_from(obj, a_class):
    '''Check if obj is an instance of a subclass of a_class
    but not an instance of a_class itself'''
    return isinstance(obj, a_class) and obj.__class__ != a_class
