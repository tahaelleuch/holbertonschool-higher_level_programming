#!/usr/bin/python3
"""<<Rectangle>> module that inherits a class"""


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


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """inisialisation of a rectangle class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
