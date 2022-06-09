#!/usr/bin/python3
""" Write a class Student that defines a student
by: (based on 10-student.py) """


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        new_dic = {}
        dic = vars(self)
        if attrs is None:
            return self.__dict__
        for name in dic:
            for key in attrs:
                if(name == key):
                    new_dic[name] = dic.get(name)
        return new_dic

    def reload_from_json(self, json):
        
