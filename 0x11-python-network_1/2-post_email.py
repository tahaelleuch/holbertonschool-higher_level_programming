#!/usr/bin/python3
"""POST an email"""

from sys import argv
from urllib import parse, request

if __name__ == "__main__":
    values = {'email': argv[2]}
    data = parse.urlencode(values).encode('utf-8')
    with urllib.request.urlopen(argv[1], data) as response:
        print(response.read().decode("utf8"))
