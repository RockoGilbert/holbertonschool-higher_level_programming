#!/usr/bin/python3
"""creates class rectangle"""


class Rectangle:
    """ class rectangle"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__height <= 0 or self.width <= 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))
        newString = ''

    def __str__(self):
        newString = ''
        if self.__height == 0 or self.__width == 0:
            return newString
        for x in range(self.__height):
            for y in range(self.__width):
                newString += "#"
            newString += "\n"
        return newString[:-1]

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
