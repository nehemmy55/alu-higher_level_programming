#!/usr/bin/python3
"""Define and define square"""


class Square:
    """Creates class square.
    Private instance  size
    """

    def __init__(self, size=0):
        """Initialization."""
        self.__size = size

    @property
    def size(self):
        """Retrieve size by getter ."""
        return self.__size

    @size.setter
    def size(self, value):
        """use Setter."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns  area sqaure."""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
