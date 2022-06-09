#!/usr/bin/python3
""" function that creates an Object from a “JSON file”"""


import json


def load_from_json_file(filename):
    """method load_from_json_file"""

    with open(filename, 'r', encoding="utf-8") as f:
        s = json.load(f)
    return (s)
