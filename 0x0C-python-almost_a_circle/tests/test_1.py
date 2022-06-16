#!/usr/bin/python3
""" Check """
import unittest
from models.rectangle import Rectangle
from models.base import Base


class  TestStringMethods (unittest . TestCase):
    "Test Class General"

    if __name__ == '__main__':

        def  test_id(self):
            "method test_id"

            b1 = Base()
            self.assertEqual(b1.id, 1)

            b2 = Base()
            self.assertEqual(b1.id, 2)

            b3 = Base()
            self.assertEqual(b1.id, 3)

            b4 = Base(12)
            self.assertEqual(b1.id, 12)

            b5 = Base()
            self.assertEqual(b1.id, 4)

            r1 = Rectangle(10, 2)
            self.assertEqual(b1.id, 1)

            r2 = Rectangle(2, 10)
            self.assertEqual(b1.id, 2)

            r3 = Rectangle(10, 2, 0, 0, 12)
            self.assertEqual(b1.id, 12)

        def  test_width_heigth(self):
            "method width_heigth"

            with self.assertRaises(TypeError):
                Rectangle(10, "2")
                
            with self.assertRaises(ValueError):
                Rectangle(-10, 2)

            with self.assertRaises(ValueError):
                Rectangle(2, -10)
