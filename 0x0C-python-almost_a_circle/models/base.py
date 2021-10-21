#!/usr/bin/python3
"""This modules defines class Base"""


import json


class Base:
    """Defining class Base and setting constructor"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # These validators are for error messages

    def integerValidator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    # X and Y Validator

    def xyValidator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    # StaticMethod for JSON rep of list_dictionaries

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    # ClassMethod that writes JSON rep of list_objs to a file

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + '.json'
        newList = []

        for item in list_objs:
            newList.append(item.to_dictionary())

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(newList))

    # StaticMethod that returns the list of JSON rep(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or 0:
            return []
        return json.loads(json_string)

    # ClassMethod that returns an instance with all attributes set

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1, 0, 0)

        if cls.__name__ is "Square":
            dummy = cls(1, 0, 0)

        dummy.update(**dictionary)
        return dummy

    # ClassMethod that returns a list of instances

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'
        newList = []

        try:
            with open(filename, 'r') as f:
                newList = cls.from_json_string(f.read())
                for i, j in enumerate(newList):
                    newList[i] = cls.create(**newList[i])
            return newList

        except:
            return []
