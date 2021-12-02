#!/usr/bin/python3
""" Task 8 """

import requests
from sys import argv

if __name__ == "__main__":

    if len(argv) > 1:
        params = {'q': argv[1]}
    else:
        params = {'q': ""}

    url = "http://0.0.0.0:5000/search_user"
    try:
        json_dict = requests.post(url, params).json()
        if len(json_dict) == 0:
            print("No result")
        else:
            print("[{id}] {name}".format(**json_dict))
    except:
        print("Not a valid JSON")
    