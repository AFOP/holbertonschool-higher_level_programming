#!/usr/bin/python3
for num in range(0, 100):
    none = num / 10
    ntwo = num % 10
    if num == 89:
        print("{:02d}".format(num))
        break
    elif none != ntwo and none < ntwo:
        print("{:02d}".format(num), end=", ")
