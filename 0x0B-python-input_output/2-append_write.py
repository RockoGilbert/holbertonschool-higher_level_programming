#!/usr/bin/python3
"""Appends file text
"""


def append_write(filename="", text=""):
    """appends string and returns count of text"""

    with open(filename, 'a', encoding='utf=8') as appendFile:
        appendFile.write(text)
        return len(text)
