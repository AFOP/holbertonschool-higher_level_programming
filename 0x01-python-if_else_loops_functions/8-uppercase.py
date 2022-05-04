#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) in range(97, 123):
            resta = 32
        else:
            resta = 0
        print('{:c}'.format(ord(c) - resta), end="")
    print()
