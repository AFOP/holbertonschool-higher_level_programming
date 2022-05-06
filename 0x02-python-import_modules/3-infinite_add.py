#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    temp = 0
    ntwo = 0
    for i in range(1, len(argv)):
        none = int(argv[i])
        result = none + ntwo
        ntwo = result
        temp = result
    print("{:d}".format(temp))
