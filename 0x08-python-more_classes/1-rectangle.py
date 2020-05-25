#!/usr/bin/python3
"""Definition of Rectangle Class"""


class Rectangle:
    """Representation of Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the Rectangle
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter of width
        Return:
            the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of width
        Args:
            value (int): width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if 0 > value:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter of height
        Return:
            the height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of height
        Args:
            value (int): height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if 0 > value:
            raise ValueError("height must be >= 0")
        self.__height = value
