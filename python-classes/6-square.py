#!/usr/bin/python3
"""Define and declare square"""


class Square:
    """Creates class square.
    Private instance  size
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialization."""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieve size by getters."""
        return self.__size

    @size.setter
    def size(self, value):
        """use setter to set value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __init__(self, size=0, position=(0, 0)):
        """Initialization."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves size by getters."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setters set  the size to value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position by getter."""
        return self.__position

    @position.setter
    def position(self, value):
        """use setters method."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current sqaure area."""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for n in range(self.__size):
                for m in range(self.__position[0]):
                    print(' ', end="")
                for o in range(self.__size):
                    print("#", end="")
                print()i
