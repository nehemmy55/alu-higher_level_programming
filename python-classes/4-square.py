#!/usr/bin/python3
"""Define and declare square"""


class Square:
    """Creates a class square.
    Private instance size
    """

    def __init__(self, size=0):
        """Initialization."""
        self.__size = size

    @property
    def size(self):
        """Retrieve size by getter."""
        return self.__size

    @size.setter
    def size(self, value):
        """use setter method size to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area square."""
        return self.__size ** 2
