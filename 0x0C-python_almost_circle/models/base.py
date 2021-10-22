#!/usr/bin/python3
"""base
"""

import json


class Base:
    """Base of the other shapes
    """
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def integer_validator(self, name, value):
        """integer_validator"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

    def xyValidator(self, name, value):
        """xyValidator"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation"""

        newLd = []
        if list_dictionaries is None:
            return newLd
        else:
            newLd = json.dumps(list_dictionaries)
        return newLd

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a dict in json to a new file"""
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
        """Json to dictionary"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a new class"""
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1, 0, 0)

        if cls.__name__ is "Square":
            dummy = cls(1, 0, 0)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads from a file"""
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
