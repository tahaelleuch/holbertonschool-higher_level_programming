#!/usr/bin/python3
"""text indetation"""


def text_indentation(text):
    """a function taht split text into lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for i in text:
        if flag == 0:
            if i == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if i in ['.', '?', ':']:
                print("{}\n".format(i))
                flag = 0
            else:
                print(i, end="")
