#!/usr/bin/python3
"""class Rectangle that defines a rectangle """


class Rectangle:
    """Function that defines a rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

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
                text.append(str(self.print_symbol))
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

    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangle areas
        """

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.__width * rect_1.__height
        area_2 = rect_2.__width * rect_2.__height
        if area_1 == area_2:
            return rect_1
        elif area_1 > area_2:
            return rect_1
        else:
            return rect_2

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

    @classmethod
    def square(cls, size=0):
        """evalue the height now value"""
        return cls(size, size) 

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
