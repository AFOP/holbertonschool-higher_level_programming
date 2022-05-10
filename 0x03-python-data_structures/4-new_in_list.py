#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list or not element:
        pass
    else:
        if idx <= 0:
            return(my_list.copy())
        if idx > len(my_list):
            return(my_list.copy())
        temp = my_list.copy()
        for i in range(len(temp)):
            if (i == idx):
                temp[i] = element
            continue
        return(temp)
