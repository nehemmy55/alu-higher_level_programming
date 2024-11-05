#!/usr/bin/python3
"""Define and declare square"""


class Square:
    """Creates class square.
    Private instance size
    """

    def __init__(self, size=0):
        """Initialization."""
        self.__size = size

    @property
    def size(self):
        """Retrieve size by getter method ."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size to valueby setters."""
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        elif value < 0:
            raise ValueError("size must be greater or equal 0")
        self.__size = value

    def area(self):
        """Returns arae of spauare"""
        return self.__size ** 2
