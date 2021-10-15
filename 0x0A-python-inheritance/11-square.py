#!/usr/bin/python3
"""Defines class from inherited class"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """creating the class square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
