#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return (None)
    new_tuple = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_tuple += [True]
        else:
            new_tuple += [False]
    return (new_tuple)
