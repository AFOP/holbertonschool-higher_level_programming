#!/usr/bin/python3
"""function that writes an Object to a
text file, using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file"""

    sj = json.dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as f:
        s = f.write(sj)
    return s
