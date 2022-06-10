#!/usr/bin/python3
""" class BaseGeometry. """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square inhered of Rectangle"""

    def __init__(self, size):
        """ method constructor """

        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """method magic str"""

        return ("[Rectangle] {}/{}".format(self.__size, self.__size))

    def area(self):
        """ method area """

        return self.__size ** 2
