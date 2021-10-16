#!/usr/bin/python3
"""This Module writes a string and returns number of characters written"""


def write_file(filename="", text=""):
    """Writes and counts the characters of a string"""
    
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)i
