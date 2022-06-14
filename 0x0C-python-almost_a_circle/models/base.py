#!/usr/bin/python3
"""Create a folder named models with an empty file __init__.py inside
- with this file, the folder will become a Python package"""

import json

class Base:
    """Class Base"""

    __nb_objects = 0
    
    def __init__(self, id=None):
        """method constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """method to_json_string"""
        return json.dumps(list_dictionaries)

