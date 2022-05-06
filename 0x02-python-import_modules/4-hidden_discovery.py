#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for nomb in dir(hidden_4):
        if nomb[0] != "_":
            print("{:s}".format(nomb))
