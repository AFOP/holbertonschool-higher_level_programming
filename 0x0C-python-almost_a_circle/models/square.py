#!/usr/bin/python3
"""Class Square inherits from Rectangle"""


from models.rectangle import Rectangle

class Square(Rectangle):
    """Class Square inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """method constructor"""

        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        """method should return [Square] (<id>) 
        <x>/<y> - <size> - in our case, 
        width or height"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))
