#!/usr/bin/python3
"""class Rectangle that defines a rectangle """


class Rectangle:
    """Function that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """evalue the width now value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """evalue the height now value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """return area"""
        return self.width * self.height

    def perimeter(self):
        """return perimeter"""
        return (self.width + self.width + self.height + self.height)
