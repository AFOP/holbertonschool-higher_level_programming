#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """method read_file"""

    with open(filename, 'r', encoding="utf-8") as f:
        s = f.read()
        print(s, end="")
