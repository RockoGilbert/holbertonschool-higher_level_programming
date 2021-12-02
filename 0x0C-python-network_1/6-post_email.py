#!/usr/bin/python3
""" Task 6 """

import requests
from sys import argv


if __name__ == "__main__":

    url = argv[1]
    params = {'email': argv[2]}
    r = requests.post(url, data=params)
    print(r.text)
