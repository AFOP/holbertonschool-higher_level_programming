#!/usr/bin/python3
""" Check """
import unittest
from models.rectangle import Rectangle
from models.base import Base


class  TestStringMethods (unittest . TestCase):
    "Test Class General"

    def  test_width_heigth(self):
        "method test_width_heigth"

        with self.assertRaises(TypeError):
            Rectangle.width("w")
