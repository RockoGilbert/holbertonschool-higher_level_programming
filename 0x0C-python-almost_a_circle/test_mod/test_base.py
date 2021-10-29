#!/usr/bin/python3
"""This modules contains unittests for Base Class"""


import unittest
from unittest import result
import pep8
from models.base import Base


class TestBase(unittest.TestCase):
    """Testing Base Class"""

    # Using class method to use in unittestin

    @classmethod
    def setUpClass(cls):
        cls.b1 = Base()
        cls.b2 = Base(50)
        cls.b3 = Base(-1)
        cls.b4 = Base(12)
        cls.b5 = Base()

    @classmethod
    def tearDownClass(cls):
        del cls.b1
        del cls.b2
        del cls.b3
        del cls.b4
        del cls.b5

    # Testing if __init__ provides proper values

    def testInstantation(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 50)
        self.assertEqual(self.b3.id, -1)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 2)

    # Testing if ID's match

    def testIDmatch(self):
        b98 = Base(98)
        self.assertEqual(b98.id, 98)
        b69 = Base(69)
        self.assertEqual(b69.id, 69)

    # Testing a dictionary to json string

    def testToJsonString(self):
        listDic = [{'id': None}, {'id': 69}, {'id': -350}, {'id': 420}]
        self.assertEqual(Base.to_json_string(
            listDic), '[{"id": null}, {"id": 69}, {"id": -350}, {"id": 420}]')

    # Testing JSON to dictionary

    def testFromJsonString(self):
        JsonString = Base.to_json_string(
                [{'id': None}, {'id': 69}, {'id': -350}, {'id': 420}])
        self.assertEqual(Base.from_json_string(JsonString),
                         [{"id": None}, {"id": 69}, {"id": -350}, {"id": 420}])

    # Testing pep8 on the file

    def testPep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
                ['models/base.py', 'models/rectangle.py', 'models/square.py'])

        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
