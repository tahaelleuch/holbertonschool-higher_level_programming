#!/usr/bin/python3
"""Base Class"""

import json


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialitation of class base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to JSON string"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)
