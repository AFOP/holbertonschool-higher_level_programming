#!/usr/bin/python3
"""returns if the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """Return True or False in case Error"""

    return type(obj) is a_class
