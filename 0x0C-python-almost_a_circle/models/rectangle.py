#!/usr/bin/python3
'''Rectangle class inherits from Base'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class inherits from Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''init method for class'''
        super().__init__(id)
        self.__width = self.verify_WH("width", width)
        self.__height = self.verify_WH("height", height)
        self.__x = self.verify_XY("x", x)
        self.__y = self.verify_XY("y", y)

    @property
    def width(self):
        '''width getter'''
        return self.__width

    @width.setter
    def width(self, val):
        '''width setter'''
        self.__width = self.verify_WH("width", val)

    @property
    def height(self):
        '''height getter'''
        return self.__height

    @height.setter
    def height(self, val):
        '''height setter'''
        self.__height = self.verify_WH("height", val)

    @property
    def x(self):
        '''x getter'''
        return self.__x

    @x.setter
    def x(self, val):
        '''x setter'''
        self.__x = self.verify_XY("x", val)

    @property
    def y(self):
        '''y getter'''
        return self.__y

    @y.setter
    def y(self, val):
        '''y setter'''
        self.__y = self.verify_XY("y", val)

    def area(self):
        '''Return area of rectangle'''
        return self.width * self.height

    def display(self):
        '''Print a representation of the rect in stdout using #'''
        if self.y:
            print("\n"*(self.y - 1))
        print("\n".join(" "*self.x+"#"*self.width for i in range(self.height)))

    def __str__(self):
        '''str representation of obj'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        '''Set values of self based on args or kwargs'''
        attr = ('id', 'width', 'height', 'x', 'y')
        if len(args) != 0:
            for i in range(len(args)):
                setattr(self, attr[i], args[i])
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        '''Return dict of obj values'''
        return {key.replace('_Rectangle__', ''): vars(self)[key]
                for key in vars(self)}
