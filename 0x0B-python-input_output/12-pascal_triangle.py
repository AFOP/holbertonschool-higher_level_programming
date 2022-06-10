#!/usr/bin/python3
""" that returns a list of lists of integers
representing the Pascal triangle of n """


def pascal_triangle(n):
    """method pascal_triangle"""

    lista = [[1],[1,1]]

    for i in range(1,n):
        linea = [1]
        for j in range(0,len(lista[i])-1):
            linea.extend([ lista[i][j] + lista[i][j+1] ])
        linea += [1]
        lista.append(linea)
    return lista
