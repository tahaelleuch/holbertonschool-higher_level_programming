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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        f = cls.__name__ + ".json"
        list_o = []
        if list_objs is not None:
            for i in list_objs:
                list_o.append(cls.to_dictionary(i))
        with open(f, 'w') as file:
            file.write(cls.to_json_string(list_o))
