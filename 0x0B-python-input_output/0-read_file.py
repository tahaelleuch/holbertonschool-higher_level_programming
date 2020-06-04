#!/usr/bin/python3
"""Read a file"""


def read_file(filename=""):
    """READ A FILE"""
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
    print(read_data, end="")
