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
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.y, self.width, self.height))

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
            raise ValueError("width must be > 0")
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
            raise ValueError("height must be > 0")
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
        """print a Rectangle taking care of x and y"""
        if self.y > 0:
            for jump in range(self.y):
                print()
        if self.height > 0 and self.width > 0:
            for h in range(self.height):
                if self.x > 0:
                    for spaces in range(self.x):
                        print(" ", end="")
                for w in range(self.width):
                    print("#", end="")
                print()
        else:
            return ("")

    def update(self, *args, **kwargs):
        """that assigns an argument to each attribute:
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute"""
        if args and args is not None:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {'id': self.id, 'width': self.__width, 'height':
                self.__height, 'x': self.__x, 'y': self.__y}
