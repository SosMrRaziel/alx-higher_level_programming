#!/usr/bin/python3
"""This is a unittest for the max_integer module"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This is a test class of methods running
    individual unittests."""
    def test_one(self):
        matrix1 = [1, 2, 3, 4]
        self.assertEqual(max_integer(matrix1), 4)

    def test_two(self):
        matrix2 = []
        self.assertEqual(max_integer(matrix2), None)

    def test_three(self):
        self.assertRaises(TypeError, max_integer, 0)

    def test_four(self):
        matrix4 = {1: 'a', 2: 'b', 3: 'c'}
        self.assertRaises(KeyError, max_integer, matrix4)

    def test_five(self):
        matrix = ['m', 'r', 'k']
        self.assertEqual(max_integer(matrix), 'r')

    def test_six(self):
        matrix = 'raziel'
        self.assertEqual(max_integer(matrix), 'z')

    def test_seven(self):
        matrix = [-80, -81, -92, -11]
        self.assertEqual(max_integer(matrix), -11)

    def test_eight(self):
        matrix1 = [5]
        self.assertEqual(max_integer(matrix1), 5)

    def test_ten(self):
        matrix1 = [3, 3, 3, 3, 3]
        self.assertEqual(max_integer(matrix1), 3)

    def test_ten(self):
        matrix1 = [3.2, 5.4, -8.6, 0.4, 17.5]
        self.assertEqual(max_integer(matrix1), 17.5)


if __name__ == '__main__':
    unittest.main()
