#!/usr/bin/python3
'''test_base.py'''

import unittest
from models.base import Base
import os


class TestBase(unittest.TestCase):
    """A class to test the Base class"""

    def setUp(self):
        """A method to set up the test cases"""
        Base._Base__nb_objects = 0  # Reset the number of objects

    def test_id(self):
        """A method to test the id attribute of the Base class"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base()
        self.assertEqual(b3.id, 2)





if __name__ == '__main__':
    unittest.main()