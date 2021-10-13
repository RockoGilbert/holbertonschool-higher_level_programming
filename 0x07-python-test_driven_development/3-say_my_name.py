#!/usr/bin/python3
"""prints first_name followed by last_name"""


def say_my_name(first_name, last_name=""):
    """prints string of first and last name"""

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
