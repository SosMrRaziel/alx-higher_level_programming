#!/usr/bin/python3
'''In the file tests/test_models/test_square.py'''

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """A class that tests the Square class"""

    def setUp(self):
        """Set up an instance of Square for testing"""
        self.square = Square(5, 2, 3, 4)

    
    def test_init(self):
        """Test the initialization of the Square instance"""

    def test_str(self):
        """Test the string representation of the Square instance"""

    
    def test_size_getter(self):
        """Test the getter for size"""


    def test_size_setter(self):
        """Test the setter for size"""

    def test_update_args(self):
        """Test the update method with *args"""

    def test_update_kwargs(self):
        """Test the update method with **kwargs"""

    def test_to_dictionary(self):
        """Test the to_dictionary method"""
    


if __name__ == "__main__":
    unittest.main()