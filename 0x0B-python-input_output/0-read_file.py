#!/usr/bin/python3
"""This module reads a file and prints it to stdout"""


def read_file(filename=""):
    """Reads a text file"""

    with open(filename, encoding="utf-8") as readFile:
        print(readFile.read(), end="")
