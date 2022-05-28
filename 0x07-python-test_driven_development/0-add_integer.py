#!/usr/bin/python3
""" add_integer: make adition integers a and b """


def add_integer(a, b=98):
    """Function that add two integers with errors of the user"""

    if (a is None and b is None):
        raise TypeError("a must be an integer")
    if (type(a) == str or a == None):
        raise TypeError("a must be an integer")
    if (type(b) == str or b == None):
        raise TypeError("b must be an integer")
    return(int(a)+int(b))
