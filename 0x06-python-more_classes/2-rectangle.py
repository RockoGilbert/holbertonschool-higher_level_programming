#!/usr/bin/python3
"""
Defines Class Rectangle
"""


class Rectangle:
    """
    Defines Rectangle by width and height
    """
    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """
        width
        args: value (int)
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """
        height
        args: value (int)
        """
        if type(value)is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        area = self.width * self.height
        return area

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        perimeter = 2 * (self.width + self.height)
        return perimeter

    def __str__(self):
        """
        __str__
        returns: printed rectangle
        """
        if self.width == 0 or self.height == 0:
            return ""
        strg = ""
        for i in range(self.height - 1):
            strg += "#" * self.width + "\n"
            if i is self.height - 2:
                strg += "#" * self.width
        return strg
