#!/usr/bin/python3
"""that defines a square by: (based on 0-square.py)"""


class Square():
    """ Class: Square """

    def __init__(self, size=0):
        """Initialize the square object
        Args:
            size (int): the size of the square"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self, size=0):
        """Initialize the square object
        Args:
            size (int): the size of the square"""
        return (self.__size ** 2)
