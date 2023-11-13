#!/usr/bin/python3
'''In the file test_rectangle.py'''

import unittest
import sys
import io
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """A class that tests the Rectangle class"""

    def test_init(self)
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

    def test_display_method_w_coordinates(self):
        """Rectangle display method unittest"""
        output = io.StringIO()
        sys.stdout = output
        r15 = Rectangle(2, 2, 2, 1)
        r15.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n  ##\n  ##\n")

    def test_str(self):
        """Test the __str__ method"""
        r = Rectangle(4, 6, 2, 1, 12)
        output = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r), output)

    def test_update(self):
        """Test the update method"""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)
        r.update(89, 2)
        self.assertEqual(r.width, 2)
        r.update(89, 2, 3)
        self.assertEqual(r.height, 3)
        r.update(89, 2, 3, 4)
        self.assertEqual(r.x, 4)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.y, 5)
        r.update(height=1, width=2, x=3, y=4, id=89)
        self.assertEqual(r.height, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 89)

    def test_to_dictionary_method(self):
        """Rectangle to_dictionary method unittest"""
        r20 = Rectangle(3, 3)
        d = r20.to_dictionary()
        self.assertEqual(d['width'], 3)
        self.assertEqual(d['height'], 3)
        self.assertEqual(d['x'], 0)
        self.assertEqual(d['y'], 0)

if __name__ == '__main__':
    unittest.main()