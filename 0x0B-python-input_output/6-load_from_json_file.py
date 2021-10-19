#!/usr/bin/python3
"""Creates an object file"""

import json


def load_from_json_file(filename):
    """Creates an object file from filename"""

    with open(filename, 'r') as fd:
        return json.loads(fd.read())
