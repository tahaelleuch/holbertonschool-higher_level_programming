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

    def update(self, *args, **kwargs):
        """update the square"""
        if args:
            for i, val in enumerate(args):
                if i == 0:
                    self.id = val
                elif i == 1:
                    self.size = val
                elif i == 2:
                    self.x = val
                elif i == 3:
                    self.y = val
        elif kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """the dictionary representation of a Rectangle"""
        dict = {}
        dict["id"] = self.id
        dict["x"] = self.x
        dict["size"] = self.size
        dict["y"] = self.y
        return dict
