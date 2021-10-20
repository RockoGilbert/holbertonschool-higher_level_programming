#!/usr/bin/python3
"""save_to_json_file"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using JSON rep"""

    with open(filename, 'w') as newfile:
        newfile.write(json.dumps(my_obj))
