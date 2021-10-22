#!/usr/bin/python3
"""This modules defines class Base"""


import json


class Base:
    """Defining class Base and setting constructor"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def integerValidator(self, name, value):
        """Class integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def xyValidator(self, name, value):
        """XY validator"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """Class Method that writes JSON list"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method to save to a file"""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + '.json'
        newList = []

        for item in list_objs:
            newList.append(item.to_dictionary())

        with open(filename, 'w') as f:
            f.write(cls.to_json_string(newList))

    @staticmethod
    def from_json_string(json_string):
        """JSON String"""
        if json_string == None or 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class that returns dict"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1, 0, 0)

        if cls.__name__ == "Square":
            dummy = cls(1, 0, 0)

        dummy.update(**dictionary)
        return dummy

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
