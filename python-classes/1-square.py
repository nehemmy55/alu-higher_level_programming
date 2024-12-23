#!/usr/bin/python3
"""Define and declara class square"""


class Square:
    """Creates a class square
    Private instance size
    """

    def __init__(self, size=0):
        """ Initialization of attribute """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
