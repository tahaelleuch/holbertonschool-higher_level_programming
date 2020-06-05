#!/usr/bin/python3
"""Read n lines"""


def read_lines(filename="", nb_lines=0):
    """Read n lines of a text and prints it"""
    i = 0
    with open(filename, 'r', encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end='')
        else:
            for i, line in enumerate(f):
                if i == nb_lines:
                    break
                print(line, end='')
