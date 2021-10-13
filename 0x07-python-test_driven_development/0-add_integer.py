#!/usr/bin/python3
"""Adds 2 ints or floats cast ad ints
"""


def add_integer(a, b=98):
    '''Adds 2 ints or floats and returns them as int
    Args:
        a: first value to add
        b: second value to add
    Returns:
        int(a + b)
    '''
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    else:
        return int(round(a) + round(b))
