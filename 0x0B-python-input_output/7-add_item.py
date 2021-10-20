#!/usr/bin/bash
"""adds arguments to a Python list"""


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    xfile = load_from_json_file('add_item.json')

except:
    xfile = []

xfile += sys.argv[1:]

save_to_json_file(xfile, 'add_item.json')
