#!/usr/bin/python3
"""class Rectangle that defines a rectangle """


class Rectangle:
    """Function that defines a rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """return text with #"""
        if self.height <= 0 or self.width <= 0:
            return ("")
        text = []
        for x in range(self.height):
            for y in range(self.width):
                text.append("#")
            text.append("\n")
        text.pop()
        return "".join(text)

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
        if (self.__width > 0 and self.__height > 0):
            return (self.__width * 2 + self.__height * 2)
        else:
            return (0)

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
