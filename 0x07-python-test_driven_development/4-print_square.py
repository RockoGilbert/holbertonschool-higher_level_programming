#!/usr/bin/python3
"""prints a square"""


def print_square(size):
    """ Prints a square of length size using the hash (#) character """
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print(size * '#')
