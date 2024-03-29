#!/usr/bin/python3
""" class BaseGeometry. """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle inhered of BaseGeometry"""

    def __init__(self, width, height):
        """ method constructor """

        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
