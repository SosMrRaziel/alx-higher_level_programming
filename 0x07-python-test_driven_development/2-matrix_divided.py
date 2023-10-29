#!/usr/bin/python3
'''
This module is composed by a function that divides the numbers of a matrix
'''


def matrix_divided(matrix, div):
    """Divide each element in a matrix by a divisor.
    matrix [[]]: a list of lists of float or int.
    div (int): non-zero integer divisor.

    Returns a new matrix.
    See tests/2-matrix_divided.txt for test cases.
    """

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError('matrix must be a matrix (list of lists)' +
                        ' of integers/floats')
    for inner in matrix:
        if not isinstance(inner, list) or len(inner) == 0:
            raise TypeError('matrix must be a matrix (list of lists)' +
                            ' of integers/floats')
        if len(inner) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        for item in inner:
            if not isinstance(item, (int, float)):
                raise TypeError('matrix must be a matrix (list of lists)' +
                                ' of integers/floats')
    return [[round(item / div, 2) for item in inner] for inner in matrix]
