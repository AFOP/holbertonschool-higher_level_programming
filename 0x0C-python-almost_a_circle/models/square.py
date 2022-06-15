#!/usr/bin/python3
"""Class Square inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """method constructor"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """return size"""
        return self.width

    @size.setter
    def size(self, value):
        """evalue the size now value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be >= 0")
        else:
            self.width = value
            self.heigth = value

    def __str__(self):
        """method should return [Square] (<id>)
        <x>/<y> - <size> - in our case,
        width or height"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """*args is the list of arguments - no-keyworded arguments
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute"""
        if args and args is not None:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
