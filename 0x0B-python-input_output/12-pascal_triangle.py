#!/usr/bin/python3
'''pascal_triangle a function def pascal_triangle(n): that returns a list
of lists of integers representing the Pascal’s triangle of n'''


def pascal_triangle(n):
    ''' Returns an empty list if n <= 0'''
    if n <= 0:
        return []
    # Creates a list of lists of integers
    # representing the Pascal's triangle of n
    # The first row is always [1]
    triangle = [[1]]
    # For each row from the second to the nth
    for i in range(1, n):
        # The first element is always 1
        row = [1]
        for j in range(1, i):
            # from the second to the (i-1)th
            # The element is the sum of the two elements above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # The last element is always 1
        row.append(1)
        # Append the row to the triangle
        triangle.append(row)
    return triangle
