#!/usr/bin/python3
'''In the file test_rectangle.py'''

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """A class that tests the Rectangle class"""

    def test_init(self):
        """Test the __init__ method"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(2, 10, 1, 2, 12)
        self.assertEqual(r2.id, 12)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 2)

    def test_width(self):
        """Test the width getter and setter"""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        r.width = 5
        self.assertEqual(r.width, 5)
        with self.assertRaises(TypeError):
            r.width = "3"
        with self.assertRaises(ValueError):
            r.width = 0

    def test_height(self):
        """Test the height getter and setter"""
        r = Rectangle(10, 2)
        self.assertEqual(r.height, 2)
        r.height = 5
        self.assertEqual(r.height, 5)
        with self.assertRaises(TypeError):
            r.height = "3"
        with self.assertRaises(ValueError):
            r.height = 0

    def test_x(self):
        """Test the x getter and setter"""
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        r.x = 5
        self.assertEqual(r.x, 5)
        with self.assertRaises(TypeError):
            r.x = "3"
        with self.assertRaises(ValueError):
            r.x = -1

    def test_y(self):
        """Test the y getter and setter"""
        r = Rectangle(10, 2)
        self.assertEqual(r.y, 0)
        r.y = 5
        self.assertEqual(r.y, 5)
        with self.assertRaises(TypeError):
            r.y = "3"
        with self.assertRaises(ValueError):
            r.y = -1

    def test_area(self):
        """Test the area method"""
        r = Rectangle(10, 2)
        self.assertEqual(r.area(), 20)
        r = Rectangle(2, 10)
        self.assertEqual(r.area(), 20)
        r = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r.area(), 56)


if __name__ == '__main__':
    unittest.main()