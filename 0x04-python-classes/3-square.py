#!/usr/bin/python3
"""This module creates a class with the private attributes"""


class Square:
        """create a class Square and use __init__ to set size"""
        def __init__(self, size=0):
            '''initilizes the square after checking for valid input
            
            Args:
                size (int): the size of the square
            '''
            if type(size) is not int:
                raise TypeError("size must be an integer")
                
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
            
            def area(self):
                """returns the area of the square"""
                return self.__size * self.__size

            @property
            def size(self):
                """returns the size of the square"""
                return self.__size
            
            @size.setter
            def size(self, value):
                '''sets the size of the square
                
                Args:
                    value (int): the size of the square
                '''
                
                if type(value) is not int:
                    raise TypeError("size must be an integer")
                if value < 0:
                    raise ValueError("size must be >= 0")
                self.__size = value
