#!/usr/bin/python3
def print_matrix_integer(matrix):
    if bool(matrix) == 1:
        for i in matrix:
            print(*i)
    else:
        print("")
