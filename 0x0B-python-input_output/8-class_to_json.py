#!/usr/bin/python3
'''dic description of JSON serialized object'''


def class_to_json(obj):
    '''dic description of JSON serialized object

    Args:
        obj: obj to return the __dict__ of
    '''
    return obj.__dict__
