#!/usr/bin/python3
"""<<Same class or inherit from>> module"""


def is_kind_of_class(obj, a_class):
    """check obj class
    Return:
        True if it s the same or inherited class False otherwise
    """
    return (isinstance(obj, a_class))
