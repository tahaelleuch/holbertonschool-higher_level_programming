#!/usr/bin/python3
"""Function that print the name"""


def say_my_name(first_name, last_name=""):
    """print the giben first name and last name
    Args:
        first_name (str): the first name
        last_name (str): the last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
