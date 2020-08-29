#!/usr/bin/python3
""" displays the body of the response"""

from sys import argv
from urllib import error, request

if __name__ == '__main__':
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode("utf8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
