#!/usr/bin/python3
""" matrix_divided: 
        divides all elements of a matrix
        matrix: the matrix of main
        div: number for divide of matrix
        Return: matrix with the divition """


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix
        div: number for divide
        new: new matrix with the divition """

    if (type(div) != int and type(div) != float):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    if (type(div) == float):
        div = int(div)
    new = []
    for x in matrix:
        new.append(x[:])
    for i in range(len(new)):
        for j in range(len(new[i])):
            if (type(new[i][j]) != int and type(new[i][j]) != float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if (type(new[i][j]) == float):
                new[i][j] = int(new[i][j])
            new[i][j] = round(new[i][j] / div, 2) 
    return(new)
