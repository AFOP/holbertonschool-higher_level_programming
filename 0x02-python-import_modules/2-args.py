#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print(len(argv) - 1, "argument", end="")
    if len(argv) - 1 == 0:
        print("s.")
    else:
        if len(argv) - 1 == 1:
            print(":")
        else:
            print("s:")
        for i in range(1, len(argv)):
            print("{:d}:".format(i), argv[i])
