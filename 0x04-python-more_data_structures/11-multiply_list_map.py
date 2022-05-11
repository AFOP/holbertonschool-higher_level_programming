#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    mul = {x*number for x in my_list}
    return mul
