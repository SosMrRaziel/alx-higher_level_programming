#!/usr/bin/python3
'''In the file tests/test_models/test_square.py'''

import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):
    """A class that tests the Square class"""

    def setUp(self):
        """Set up an instance of Square for testing"""
        self.square = Square(5, 2, 3, 4)

    def test_init(self):
        """Test the initialization of the Square instance"""
        self.assertEqual(self.square.id, 4)
        self.assertEqual(self.square.size, 5)
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square.y, 3)

    def test_str(self):
        """Test the string representation of the Square instance"""
        self.assertEqual(str(self.square), "[Square] (4) 2/3 - 5")

    def test_size_getter(self):
        """Test the getter for size"""
        self.assertEqual(self.square.size, 5)

    def test_size_setter(self):
        """Test the setter for size"""
        self.square.size = 10
        self.assertEqual(self.square.size, 10)
        self.assertEqual(self.square.width, 10)
        self.assertEqual(self.square.height, 10)
        with self.assertRaises(TypeError):
            self.square.size = "hello"
        with self.assertRaises(ValueError):
            self.square.size = -1

    def test_update_args(self):
        """Test the update method with *args"""
        self.square.update(10, 20, 30, 40)
        self.assertEqual(self.square.id, 10)
        self.assertEqual(self.square.size, 20)
        self.assertEqual(self.square.x, 30)
        self.assertEqual(self.square.y, 40)

    def test_update_kwargs(self):
        """Test the update method with **kwargs"""
        self.square.update(id=100, size=200, x=300, y=400)
        self.assertEqual(self.square.id, 100)
        self.assertEqual(self.square.size, 200)
        self.assertEqual(self.square.x, 300)
        self.assertEqual(self.square.y, 400)

    def test_to_dictionary(self):
        """Test the to_dictionary method"""
        square_dict = self.square.to_dictionary()
        self.assertEqual(square_dict["id"], 4)
        self.assertEqual(square_dict["size"], 5)
        self.assertEqual(square_dict["x"], 2)
        self.assertEqual(square_dict["y"], 3)
        self.assertIsInstance(square_dict, dict)

if __name__ == "__main__":
    unittest.main()