#!/usr/bin/python3
"""My list module"""


class MyList(list):
    """inhirate from list"""

    def __init__(self):
        """initialisate the object"""
        super().__init__()

    def print_sorted(self):
        """print the list"""
        print(sorted(self))
