#!/usr/bin/python3
def islower(c):
    for lower in range(ord('a'), ord('z')+1):
        if lower == ord(c):
            return (True)
            break
    else:
        return (False)
