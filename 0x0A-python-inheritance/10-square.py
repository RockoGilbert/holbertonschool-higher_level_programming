#!/usr/bin/python3
"""Class that inherits from a rectangle"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Creatingthe Class square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.size = size

    def area():
        return self.__size * self.__size
