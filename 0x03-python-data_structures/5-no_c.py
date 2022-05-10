#!/usr/bin/env python3
def no_c(my_string):
    i = 0
    temp = ""
    for x in range(len(my_string)):
        if my_string[x] != "c" and my_string[x] != "C":
            temp += my_string[x]
        continue
    return (temp)
