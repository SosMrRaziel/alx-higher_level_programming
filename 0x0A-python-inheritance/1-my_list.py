#!/usr/bin/python3
''' class Mylist'''


class MyList(list):
    """A class that inherits from list and has a print_sorted method"""
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""

        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
