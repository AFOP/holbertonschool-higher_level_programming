#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    sum = 0
    for i in range(len(my_list)):
        x = my_list[i]
        if x not in new:
            new.append(x)
    for j in range(len(new)):
        sum += new[j]
    return sum
