#!/usr/bin/python3
"""This module tests the Rectangle class"""


import unittest
import pep8
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Testing the Rectangle Class"""

    @classmethod
    def setUpClass(cls):
        """Setting up class"""
        cls.r1 = Rectangle(10, 5)
        cls.r2 = Rectangle(69, 420, 350, 15)
        cls.r3 = Rectangle(6, 12, 18, 24, 30)
        cls.r4 = Rectangle(50, 150)

    @classmethod
    def tearDownClass(cls):
        """Tearing down class"""
        del cls.r1
        del cls.r2
        del cls.r3
        del cls.r4

    def testInstantation(self):
        """Testing init values"""
        self.assertEqual(self.r1.id, 3)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 5)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)

        self.assertEqual(self.r2.id, 4)
        self.assertEqual(self.r2.width, 69)
        self.assertEqual(self.r2.height, 420)
        self.assertEqual(self.r2.x, 350)
        self.assertEqual(self.r2.y, 15)

        self.assertEqual(self.r3.id, 30)
        self.assertEqual(self.r3.width, 6)
        self.assertEqual(self.r3.height, 12)
        self.assertEqual(self.r3.x, 18)
        self.assertEqual(self.r3.y, 24)

        self.assertEqual(self.r4.id, 5)
        self.assertEqual(self.r4.width, 50)
        self.assertEqual(self.r4.height, 150)
        self.assertEqual(self.r4.x, 0)
        self.assertEqual(self.r4.y, 0)

    def testInitErrors(self):
        """The init errors tested"""
        with self.assertRaises(TypeError):
            """Testing typeerrors"""
            r5 = Rectangle()
            r5 = Rectangle("String")
            r6 = Rectangle(5)
            r6 = Rectangle(5, "String")
            r6 = Rectangle(5, 6, "String")
            r6 = Rectangle(5, 6, 7, "String")
            r6 = Rectangle(5, 6, 7, 8, "String")

        with self.assertRaises(ValueError):
            """Testing valueerrors"""
            r7 = Rectangle(0, 1, id=0)
            r7 = Rectangle(0, 0, id=0)
            r7 = Rectangle(1, 0, id=0)
            r7 = Rectangle(-1, 1, id=0)
            r7 = Rectangle(1, -1, id=0)
            r7 = Rectangle(1, 1, -1, id=0)
            r7 = Rectangle(1, 1, 1, -1, id=0)

        def testSetter(self):
            """Testing setter"""
            R = Rectangle(1, 1)
            R.id = 69
            self.assertEqual(R.id, 69)
            R.width = 420
            self.assertEqual(R.width, 420)
            R.height = 350
            self.assertEqual(R.height, 350)
            R.x = 10
            self.assertEqual(R.x, 10)
            R.y = 15
            self.assertEqual(R.y, 15)

        def TestSetterErrors(self):
            """Testing setter errors"""
            self.assertRaises(TypeError, self.R.__init__, ["5", "6"])
            self.assertRaises(TypeError, self.R.__init__, [[5], [6]])
            self.assertRaises(TypeError, self.R.__init__, [5.69420, 6.35069])
            self.assertRaises(TypeError, self.R.__init__, [{5}, {6}])
            self.assertRaises(TypeError, self.R.__init__, [(5,), (6,)])
            self.assertRaises(TypeError, self.R.__init__, [None, None])

            self.assertRaises(ValueError, self.R.width, -1)
            self.assertRaises(ValueError, self.R.height, -1)
            self.assertRaises(ValueError, self.R.x, -1)
            self.assertRaises(ValueError, self.R.y, -1)

        def testArea(self):
            """Testing area"""
            R = Rectangle(5, 10, id=0)
            self.assertEqual(R.area(), 50)
            R.width = 3
            self.assertEqual(R.area(), 30)
            R.height = 5
            self.assertEqual(R.area(), 15)

        def testUpdateArgs(self):
            """Testing update with args"""
            R = Rectangle(2, 2, id=0)
            self.assertEqual(R.id, 0)
            self.assertEqual(R.width, 2)
            self.assertEqual(R.height, 2)
            self.assertEqual(R.x, 0)
            self.assertEqual(R.y, 0)

            R.update(69)
            self.assertEqual(R.id, 69)
            self.assertEqual(R.width, 2)
            self.assertEqual(R.height, 2)
            self.assertEqual(R.x, 0)
            self.assertEqual(R.y, 0)

            R.update(350, 420)
            self.assertEqual(R.id, 350)
            self.assertEqual(R.width, 420)
            self.assertEqual(R.height, 2)
            self.assertEqual(R.x, 0)
            self.assertEqual(R.y, 0)

            R.update(69, 350, 420)
            self.assertEqual(R.id, 69)
            self.assertEqual(R.width, 350)
            self.assertEqual(R.height, 420)
            self.assertEqual(R.x, 0)
            self.assertEqual(R.y, 0)

            R.update(1, 2, 3, 4)
            self.assertEqual(R.id, 1)
            self.assertEqual(R.width, 2)
            self.assertEqual(R.height, 3)
            self.assertEqual(R.x, 4)
            self.assertEqual(R.y, 0)

            R.update(10, 9, 8, 7, 6)
            self.assertEqual(R.id, 10)
            self.assertEqual(R.width, 9)
            self.assertEqual(R.height, 8)
            self.assertEqual(R.x, 7)
            self.assertEqual(R.y, 6)

        def testUpdateKWARGS(self):
            """Testing update with KWARGS"""
            R = Rectangle(2, 2, id=0)
            self.assertEqual(R.id, 0)
            self.assertEqual(R.width, 2)
            self.assertEqual(R.height, 2)
            self.assertEqual(R.x, 0)
            self.assertEqual(R.y, 0)

            R.update(width=69, id=420)
            self.assertEqual(R.id, 420)
            self.assertEqual(R.width, 69)
            self.assertEqual(R.height, 2)
            self.assertEqual(R.x, 0)
            self.assertEqual(R.y, 0)

            R.update(x=5, width=350, y=10, id=69, height=420)
            self.assertEqual(R.id, 69)
            self.assertEqual(R.width, 350)
            self.assertEqual(R.height, 420)
            self.assertEqual(R.x, 5)
            self.assertEqual(R.y, 10)

        def testCreate(self):
            """Testing create"""
            R = Rectangle(5, 4, 3, 2, 1)
            R_dic = R.to_dictionary()
            R2 = Rectangle.create(**R_dic)
            self.assertEqual(R2.id, 1)
            self.assertEqual(R2.width, 5)
            self.assertEqual(R2.height, 4)
            self.assertEqual(R2.x, 3)
            self.assertEqual(R2.y, 2)

        def testPep8(self):
            """Testing pep8 on file"""
            pep8style = pep8.StyleGuide(quiet=True)
            result = pep8style.check_files(
                    ['models/base.py', 'models/rectangle.py',
                        'models/square.py'])

            self.assertEqual(result.total_errors, 0,
                             "Found code style errors (and warnings).")i
