#!/usr/bin/python3
"""Define aand declare class square"""


class Square:
    """Creates a class square
    Private instance size
    """

    def __init__(self, size=0):
        """Initialization """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be greater than 0")
        self.__size = size
