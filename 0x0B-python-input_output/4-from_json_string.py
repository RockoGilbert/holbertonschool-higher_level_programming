#!/usr/bin/python3
"""from json string
"""
import json


def from_json_string(my_str):
    """ return JSON format of my_str"""
    return json.loads(my_str)
