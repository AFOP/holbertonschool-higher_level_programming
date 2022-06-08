#!/usr/bin/python3
""" class BaseGeometry. """


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """method area"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """integer validator"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class Rectangle inhered of BaseGeometry"""

    def __init__(self, width, height):
        """ method constructor """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """method area"""

        return self.__width * self.__height

    def __str__(self):
        """method magic str"""

        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """class Square inhered of Rectangle"""

    def __init__(self, size):
        """ method constructor """

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ method area """

        return self.__size **2
