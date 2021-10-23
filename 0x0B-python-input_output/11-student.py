#!/usr/bin/python3
"""
Write a class Student that defines a student by: (based on 10-student.py)
"""


class Student:
    """class student student"""

    def __init__(self, first_name, last_name, age):
        """class specifications for student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictonary reps of student class"""


        strs = {}


        if attrs is not None:
            for varis in attrs:
                if varis in self.__dict__:
                    strs[varis] = self.__dict__[varis]
                return strs
            else:
                return vars(self)


    def reload_from_json(self, json):
        self.__dict__ = json
