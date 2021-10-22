#!/usr/bin/python3
'''
Rectangle class
'''


from models.base import Base


class Rectangle(Base):
    """Rectangle Class inherited from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init for self width height x and y"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area for the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints # characters"""
        for horiz in range(self.__y):
            print("")
        for horiz in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """overrides the str method"""
        return("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """assigns arg to each attr"""
        a_list = ["id", "width", "height", "x", "y"]
        if args and args[0] is not None:
            for rang in range(len(args)):
                setattr(self, a_list[rang], args[rang])

    def to_dictionary(self):
        """returns dictionary rep"""
        the_dict = {}

        the_dict['id'] = self.id
        the_dict['width'] = self.width
        the_dict['height'] = self.height
        the_dict['x'] = self.__x
        the_dict['y'] = self.__y

        return the_dict
