#!/usr/bin/python3
"""Can I? module"""


def add_attribute(obj, name, value):
    """adds a new attribute to an object if its possible"""
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
