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

    def __str__(self):
        """method should return [Square] (<id>) 
        <x>/<y> - <size> - in our case, 
        width or height"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))
