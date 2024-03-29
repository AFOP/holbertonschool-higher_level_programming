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
