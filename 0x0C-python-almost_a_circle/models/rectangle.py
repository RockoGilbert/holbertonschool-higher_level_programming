#!/usr/bin/python3
'''Rectangle class inherits from Base'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class inherits from Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = self.verify_WH("width", width)
        self.__height = self.verify_WH("height", height)
        self.__x = self.verify_XY("x", x)
        self.__y = self.verify_XY("y", y)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        self.__width = self.verify_WH("width", val)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        self.__height = self.verify_WH("height", val)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = self.verify_XY("x", val)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.__y = self.verify_XY("y", val)

    def area(self):
        return self.width * self.height

    def display(self):
        if self.y:
            print("\n"*(self.y - 1))
        print("\n".join(" "*self.x+"#"*self.width for i in range(self.height)))

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        attr = ('id', 'width', 'height', 'x', 'y')
        if len(args) != 0:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        return {key.replace('_Rectangle__', ''): vars(self)[key]
                for key in vars(self)}
