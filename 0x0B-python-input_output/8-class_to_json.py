#!/usr/bin/python3
"""  Write a function that returns the dictionary 
description with simple data structure 
(list, dictionary, string, integer and boolean)
for JSON serialization of an object """


def class_to_json(obj):
    """method class_to_json"""

    return(vars(obj))
