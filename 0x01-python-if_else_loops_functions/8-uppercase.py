#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        for a in range (97, 123):
            if ord(str[c]) == a:
                resta = 32
                break
            else:
                resta = 0
                break
        print('{:c}'.format(ord(str[c]) - resta), end="")
