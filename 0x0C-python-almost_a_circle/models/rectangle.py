#!/usr/bin/python3
"""This module defines class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Defining Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.integerValidator("width", width)
        self.__width = width
        self.integerValidator("height", height)
        self.__height = height
        self.xyValidator("x", x)
        self.__x = x
        self.xyValidator("y", y)
        self.__y = y

    # Getter for width

    @property
    def width(self):
        return self.__width

    # Setter for width w/ validator

    @width.setter
    def width(self, value):
        self.integerValidator("width", value)
        self.__width = value

    # Getter for height

    @property
    def height(self):
        return self.__height

    # Setter for height w/ validator

    @height.setter
    def height(self, value):
        self.integerValidator("height", value)
        self.__height = value

    # Getter for x"""

    @property
    def x(self):
        return self.__x

    # Setter for x w/ validator

    @x.setter
    def x(self, value):
        self.xyValidator("x", value)
        self.__x = value

    # Getter for y"""

    @property
    def y(self):
        return self.__y

    # Setter for y w/ validator

    @y.setter
    def y(self, value):
        self.xyValidator("y", value)
        self.__y = value

    # Gets and returns area

    def area(self):
        return self.__height * self.__width

    # Displays the rectangle

    def display(self):
        for row in range(self.__y):
            print("")
        for col in range(self.__height):
            print(" "*self.__x, end="")
            print("#"*self.__width)

    # Overrides string rep to what we want

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    # Assigns an argument to each attribute

    def update(self, *args, **kwargs):
        Attributes = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) != 0:
            for key in range(len(args)):
                setattr(self, Attributes[key], args[key])

        else:
            for item in kwargs:
                setattr(self, item, kwargs[item])

    # Dictionary rep of the class

    def to_dictionary(self):
        Dic = {'id': self.id, 'width': self.width,
               'height': self.height, 'x': self.x, 'y': self.y}
        return Dic
