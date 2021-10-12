#!/usr/bin/python3
"""
A function that adds 2 integers

"""


def add_integer(a, b=98):
    """ checks if type is integer if int return sum"""
    if isinstance(a, float):
        a=int(a)
    if isinstance(b, float):
        b=int(b)
    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
    else:
        return a + b
