#!/usr/bin/python3
""" Defines a class Square by size"""


class Square:
    """ Defines an object size """
    def __init__(self, size=0):
        self.__size = size
        @property
        def size(self):
            return self.__size
        @size.setter
        def size(self, value):
            self.__size = value
            if type(value) is not int:
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            def area(self):
                return self.__size * self.__size
