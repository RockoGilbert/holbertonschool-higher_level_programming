#!/usr/bin/python3
'''Rectangle class inherits from Base'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class inherits from Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        """setting attributes"""

        super().__init__(id)
        self.__width = self.verify_WH("width", width)
        self.__height = self.verify_WH("height", height)
        self.__x = self.verify_XY("x", x)
        self.__y = self.verify_XY("y", y)

    @property
    def width(self):
        """property of width"""

        return self.__width

    @width.setter
    def width(self, val):
        """Setting width"""

        self.__width = self.verify_WH("width", val)

    @property
    def height(self):
        """Property of height"""

        return self.__height

    @height.setter
    def height(self, val):
        """setting height"""

        self.__height = self.verify_WH("height", val)

    @property
    def x(self):
        """Property of property"""

        return self.__x

    @x.setter
    def x(self, val):
        """Setting X"""
        self.__x = self.verify_XY("x", val)

    @property
    def y(self):
        """Property of Y"""

        return self.__y

    @y.setter
    def y(self, val):
        """Setting Y"""

        self.__y = self.verify_XY("y", val)

    def area(self):
        """Computing Area"""

        return self.width * self.height

    def display(self):
        """Display function"""

        if self.y:
            print("\n"*(self.y - 1))
        print("\n".join(" "*self.x+"#"*self.width for i in range(self.height)))

    def __str__(self):
        """adding strings"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updating arguments"""

        attr = ('id', 'width', 'height', 'x', 'y')
        if len(args) != 0:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """replacing variable"""

        return {key.replace('_Rectangle__', ''): vars(self)[key]
                for key in vars(self)}
