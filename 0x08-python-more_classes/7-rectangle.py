#!/usr/bin/python3
"""Definition of Rectangle Class"""


class Rectangle:
    """Representation of Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the Rectangle
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Get the area of the Rectangle
        Return:
            The area
        """
        return self.__width * self.__height

    def perimeter(self):
        """Get the perimeter of the Rectangle
        Return:
            The perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """A string represntation of the Rectangle
        Return:
            The Rectangle as string type
        """
        rec = ""
        if self.__width != 0 or self.__height != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    rec = rec + str(self.print_symbol)
                if i != (self.__height - 1):
                    rec = rec + "\n"
        return rec

    def __repr__(self):
        """A represntation of the Rectangle
        Return:
            The representation
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when a parametre is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
