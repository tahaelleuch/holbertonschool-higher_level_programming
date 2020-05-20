#!/usr/bin/python3
"""Definition of a class square"""


class Square:
    """Represntation of a square"""
    def __init__(self, size=0):
        """Initializes the square
        Args:
            size (int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Return the square area

        Returns:
            The area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Get __size
        Returns:
            size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size

        Args:
            size (int): size of size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
