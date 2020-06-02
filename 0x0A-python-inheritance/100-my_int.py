#!/usr/bin/python3
"""module My integer that inherits int"""


class MyInt(int):
    """a new integer class"""
    def __init__(self, value):
        """inisialisation of MyInt"""
        if type(value) is not int:
            raise TypeError("must be an integer")
        self.__value = value

    def __new__(cls, *args, **kwargs):
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """chnaging equality"""
        return int(self) != other

    def __ne__(self, other):
        """changing inequality"""
        return int(self) == other
