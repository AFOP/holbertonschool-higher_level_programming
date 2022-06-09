#!/usr/bin/python3
""" that returns a list of lists of integers
representing the Pascal triangle of n """


def pascal_triangle(n):
    """method pascal_triangle"""

    new_list = []
    i = 0
    j = 1

    for i in range(n):
        new_list.append([[]])
        new_list[i].append(1)
        for j in range(1, i):
            new_list[i].append(new_list[i-1][j-1] + new_list[i-1][j])
        if i != 0:
            new_list[i].append(1) 
    return new_list
