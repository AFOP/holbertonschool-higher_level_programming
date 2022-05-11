#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    llave = list(a_dictionary.keys())
    for i in llave:
        new[i] *= 2
    return new
