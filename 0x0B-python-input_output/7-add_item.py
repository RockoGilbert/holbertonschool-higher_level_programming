#!/usr/bin/python3
'''Save all args from list to file'''

import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    add_json = load_from_json_file('add_item.json')
except:
    add_json = []

add_json += sys.argv[1:]

save_to_json_file(add_json, 'add_item.json')i
