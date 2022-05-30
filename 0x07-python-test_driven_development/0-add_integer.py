#!/usr/bin/python3
""" add_integer:
        make adition integers a and b
        a: number for sum
        b: number for sum
        Return: add of a plus b """


def add_integer(a, b=98):
    """Function that add two integers with errors of the user
    a: number for sum
    b: number inicialiced to 98"""

    if (a is None):
        raise TypeError("a must be an integer")
    if (b is None):
        raise TypeError("b must be an integer")
    if (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if (type(b) != int and type(b) != float):
        raise TypeError("b must be an integer")
    if (type(a) == float):
        a = int(a)
    if (type(b) == float):
        b = int(b)
    if (type(a) == str):
        raise TypeError("a must be an integer")
    if (type(b) == str):
        raise TypeError("b must be an integer")
    return(a+b)
