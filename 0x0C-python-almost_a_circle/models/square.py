#!/usr/bin/python3
"""Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """inisialization of the square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return str representation of square"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    @property
    def size(self):
        """getter of size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter of size"""
        self.width = value
        self.height = value
