#!/usr/bin/python3
'''In the file tests/test_rectangle.py'''

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


    def test_height(self):
        """Test the height getter and setter"""

    def test_x(self):
        """Test the x getter and setter"""
    
    def test_y(self):
        """Test the y getter and setter"""

    def test_area(self):
        """Test the area method"""

    def test_display(self):
        """Test the display method"""

    def test_str(self):
        """Test the __str__ method"""

    def test_update(self):
        """Test the update method"""

    def test_to_dictionary(self):
        """Test the to_dictionary method"""

if __name__ == '__main__':
    unittest.main()