#!/usr/bin/python3
"""<<Only sub class>> module"""


def inherits_from(obj, a_class):
    """check obj class
    Return:
        True if it s only inherited class False otherwise
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
