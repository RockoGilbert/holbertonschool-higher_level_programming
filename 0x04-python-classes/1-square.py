#!/usr/bin/python
"""Defines a class based on square size"""

class Square:
    """create an object and using __init__ to set size"""
    def __init__(self, size=0):
        """initializes the square"""

        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

