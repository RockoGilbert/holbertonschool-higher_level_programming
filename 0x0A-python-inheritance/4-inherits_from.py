#!/usr/bin/python3
"""Returns true if instance of a class is inherited from a class"""


def inherits_from(obj, a_class):
    return(issubclass(type(obj), a_class) and type(obj) is not a_class)
