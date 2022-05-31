#!/usr/bin/python3
""" print_square:
        function that prints a square with the character #
        size: is the size length of the square
        Return: Nothing """


def print_square(size):
    """Write a function that prints a square with the character #
        size: is the size length of the square """

    if (type(size) != int):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
