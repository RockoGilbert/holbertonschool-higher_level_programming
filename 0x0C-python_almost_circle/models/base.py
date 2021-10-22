#!/usr/bin/python3
"""
Clas Base
"""


import json


class Base:
    """Class for file Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializing base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string rep of list_dictionaries"""
        listdict2 = []
        if list_dictionaries is None or list_dictionaries == "":
            return listdict2
        else:
            listdict2 = json.dumps(list_dictionaries)
        return listdict2
