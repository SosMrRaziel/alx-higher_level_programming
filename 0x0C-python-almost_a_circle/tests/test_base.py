#!/usr/bin/python3
'''test_base.py'''

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """A class to test the Base class"""

    def setUp(self):
        """A method to set up the test cases"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """A method to test the id attribute of Base instances"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base()
        self.assertEqual(b3.id, 2)  # Check if the id is 2

    def test_to_json_string(self):
        """A method to test the to_json_string static method of Base"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}, {'id': 5}]), '[{"id": 12}, {"id": 5}]')

    def test_from_json_string(self):
        """A method to test the from_json_string static method of Base"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string('[{"id": 12}, {"id": 5}]'), [{'id': 12}, {'id': 5}])


if __name__ == '__main__':
    unittest.main()