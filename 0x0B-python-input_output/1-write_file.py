#!/usr/bin/python3
"""function that writes a string to a text file (UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    """method write_file"""

    with open(filename, 'w', encoding="utf-8") as f:
        s = f.write(text)
    f.close()
    return s
