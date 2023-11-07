#!/usr/bin/python3
def read_file(filename=""):
    '''Use the with statement to open the file and ensure it is closed'''
    with open(filename, encoding="utf-8") as f:
        # loop through each line in the file
        for line in f:
            print(line, end="")
