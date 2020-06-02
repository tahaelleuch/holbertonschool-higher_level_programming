#!/usr/bin/python3
"""<<Integer validator>> module that define a class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Public instance that raise an Exception message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ instance method that validates value"""
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
