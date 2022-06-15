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

    @classmethod
    def save_to_file(cls, list_objs):
        """method save_to_file"""
        lista = []
        if list_objs is not None:
            for x in list_objs:
                lista.append(cls.to_dictionary(x))
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(lista))

    @staticmethod
    def from_json_string(json_string):
        """method from_json_string"""
        return json.loads(json_string)
