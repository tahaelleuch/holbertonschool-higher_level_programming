#!/usr/bin/python3
""" in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        if not req.json():
            print("No result")
        else:
            print("[{}] {}".format(req.json().get("id"), req.json().get("name")))
    except ValueError:
        print("Not a valid JSON")
