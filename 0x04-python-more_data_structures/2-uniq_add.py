#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = 0
    my_list.sort()
    for i in range(len(my_list)):
        if my_list[i-1] != my_list[i]:
            new += int(my_list[i])
    return new
