#!/usr/bin/python3
""" Check """
import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class  General(unittest.TestCase):
    "Test Class General"

    def  test_id(self):
        "method test_id"

        b1 = Base()
        self.assertEqual(b1.id, 1)

    def  test_width_heigth(self):
        "method test_width_heigth"

        with self.assertRaises(TypeError) as exc:
            Rectangle(10, "2")
        self.assertEqual(str(exc.exception), "height must be an integer")
                
        with self.assertRaises(ValueError) as exc:
            Rectangle(-10, 2)
        self.assertEqual(str(exc.exception), "width must be > 0")

        with self.assertRaises(ValueError) as exc:
            Rectangle(2, -10)
        self.assertEqual(str(exc.exception), "height must be > 0")

if __name__ == '__main__':
        unittest.main()
