#!/usr/bin/python3
"""Create a folder named models with an empty file __init__.py inside
- with this file, the folder will become a Python package"""

import json
import os.path


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
        """class method save_to_file"""
        lista = []
        if list_objs is not None:
            for x in list_objs:
                lista.append(cls.to_dictionary(x))
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(lista))

    @staticmethod
    def from_json_string(json_string):
        """static method from_json_string"""
        lista = []
        if json_string is not None:
            return json.loads(json_string)
        else:
            return lista

    @classmethod
    def create(cls, **dictionary):
        """class method from_json_string"""
        nom_class = cls.__name__
        if nom_class == 'Rectangle':
            dummy = cls(1, 1)
        if nom_class == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """class method load_from_file"""
        lista = []
        filename = cls.__name__ + ".json"
        if os.path.isfile(filename):
            with open(filename, 'r', encoding="utf-8") as file_json:
                file_str = cls.from_json_string(file_json.read())
                for x in file_str:
                    lista.append(cls.create(**x))
            return lista
        else:
            return []
