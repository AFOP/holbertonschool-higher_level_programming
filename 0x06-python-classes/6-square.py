#!/usr/bin/python3
"""that defines a square by: (based on 0-square.py)"""


class Square():
    """ Class: Square """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square object
        Args:
            size (int): the size of the square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """return size"""
        return self.__size
    @size.setter
    def size(self, value):
        """evalue the size now value"""
        if type(value) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    @property
    def position(self):
        """return size"""
        return self.__position
    @position.setter
    def position(self, value):
        """evalue the position"""
        if (type(value) != tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (len(value) != 2):
            raise ValueError("position must be a tuple of 2 positive integers")
        if (type(value[0]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0  or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self, size=0):
        """area: calculate area of size"""
        return (self.__size ** 2)

    def my_print(self):
        """area: calculate area of size"""
        if self.__size == 0:
            return print()
        if self.__position[0] >= 0 and self.__position[1] >= 0:
            for x in range(self.__position[1]):
                print()
        for f in range(0, self.__size):
            for y in range(self.__position[0]):
                print(" ", end="")
            for c in range(0, self.__size):
                print("#", end="")
            print()
