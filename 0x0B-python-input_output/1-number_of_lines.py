#!/usr/bin/python3
"""Number of lines"""


def number_of_lines(filename=""):
    """get the number of lines of a file"""
    i = 0
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            i = i + 1
    return (i)
