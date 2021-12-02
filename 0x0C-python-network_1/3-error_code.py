#!/usr/bin/python3
""" error manage module """
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.getcode()))
