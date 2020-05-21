#!/usr/bin/python3
"""Definition of a class square"""


class Square:
    """Represntation of a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square
        Args:
            size (int): size of the square
            position (tuple): the position of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter of position
        Returns:
            the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position
        Args:
            value (int): value of position
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """print a square

        Return:
            printed square
        """
        if self.__size != 0:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()
        else:
            print()

