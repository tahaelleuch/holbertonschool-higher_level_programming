#!/usr/bin/python3
"""github commit"""

import requests
from sys import argv


if __name__ == '__main__':
    req = requests.get('https://api.github.com/repos/' +
                       argv[2] + '/' + argv[1] + '/commits')
    for commit in req.json()[0:10]:
        print("{}: {}".format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))
