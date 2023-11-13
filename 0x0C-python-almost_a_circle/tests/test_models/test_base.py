#!/usr/bin/python3
'''test_base.py'''

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """A class to test the base class"""

    def setUp(self):
        """A method to set up the test cases"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """A method to test the id attribute"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        b3 = Base()
        self.assertEqual(b3.id, 2)

    def test_to_json_string(self):
        """A method to test the to_json_string static method"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{'id': 12}, {'id': 5}]), '[{"id": 12}, {"id": 5}]')

    def test_from_json_string(self):
        """A method to test the from_json_string static method"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string('[{"id": 12}, {"id": 5}]'), [{'id': 12}, {'id': 5}])

    def test_save_to_file(self):
        """A method to test the save_to_file class method"""
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 1}, {"id": 2}]')

    def test_create(self):
        """A method to test the create class method"""
        b1 = Base.create(**{'id': 89})
        self.assertEqual(b1.id, 89)

    def test_load_from_file(self):
        """A method to test the load_from_file class method"""
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        list_objs = Base.load_from_file()
        self.assertEqual(len(list_objs), 2)
        self.assertEqual(list_objs[0].id, 1)
        self.assertEqual(list_objs[1].id, 2)