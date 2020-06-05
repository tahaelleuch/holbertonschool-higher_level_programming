#!/usr/bin/python3
"""JSON"""


def from_json_string(my_str):
    """a function that returns an object represented by a JSON"""
    import json
    return (json.loads(my_str))
