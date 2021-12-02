#!/usr/bin/python3
""" Takes a URL and email, sends a POST request to URL with email as param """

from urllib import request, parse
from sys import argv

if __name__ == "__main__":

    url = argv[1]

    encoding = 'utf8'
    data = parse.urlencode({'email': argv[2]})
    data = data.encode(encoding)
    req = request.Request(url, data)

    with request.urlopen(req) as response:
        output = response.read().decode(encoding)
        print(output)
