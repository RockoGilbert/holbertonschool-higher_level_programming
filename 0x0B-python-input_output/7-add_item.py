#!/usr/bin/python3
'''Save all args from list to file'''
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    out = load_from_json_file('add_item.json')
except:
    out = []

save_to_json_file(out + sys.argv[1:], 'add_item.json')
