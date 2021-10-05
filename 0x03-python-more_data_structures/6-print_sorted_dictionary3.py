#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = a_dictionary.copy()
    for x in sorted(new_dict):
        print("{}: {}".format(x, new_dict[x]))
