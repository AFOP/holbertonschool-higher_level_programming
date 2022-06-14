#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base"""


from models.base import Base

class Rectangle(Base):
    """Class Rectangle inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """method constructor"""

        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Update the class Rectangle by overriding the 
        __str__ method so that it returns [Rectangle] 
        (<id>) <x>/<y> - <width>/<height>"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))

    @property
    def width(self):
        """return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """evalue the width now value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
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
        elif value <= 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def x(self):
        """return private x"""
        return self.__x

    @x.setter
    def x(self, value):
        """evalue the x now value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """return private y"""
        return self.__y

    @y.setter
    def y(self, value):
        """evalue the y now value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """return area"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle"""
        if self.height <= 0 or self.width <= 0:
            return ("")
        text = []
        for x in range(self.height):
            for y in range(self.width):
                print("#", end="")
            print()
