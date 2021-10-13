#!/usr/bin/python3
""" prints a square with the character #
"""


def print_square(size):
    """ Determins the paramaters of size
        and prints a square with #
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if size == 0:
        return None

    for row in range(size):
        print('#' * size)
