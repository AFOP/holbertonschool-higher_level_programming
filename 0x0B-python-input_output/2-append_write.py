#!/usr/bin/python3
"""Write a function that appends a string at the end
of a text file (UTF8) and returns the number
of characters added"""


def append_write(filename="", text=""):
    """method append_file"""

    with open(filename, 'r+', encoding="utf-8") as f:
        s = f.write(text)
    f.close()
    return s
