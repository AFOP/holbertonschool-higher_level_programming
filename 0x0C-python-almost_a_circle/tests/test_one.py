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
        self.assertEqual(b1.id, 2)

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
    
    def  test_x_y(self):
        "method test_x_y"

        with self.assertRaises(TypeError) as exc:
            Rectangle(1, 2, 3, "4")
        self.assertEqual(str(exc.exception), "y must be an integer")
                
        with self.assertRaises(TypeError) as exc:
            Rectangle(1, 2, "3", 4)
        self.assertEqual(str(exc.exception), "x must be an integer")

        with self.assertRaises(ValueError) as exc:
            Rectangle(1, 2, 3, -4)
        self.assertEqual(str(exc.exception), "y must be >= 0")

        with self.assertRaises(ValueError) as exc:
            Rectangle(1, 2, -3, 4)
        self.assertEqual(str(exc.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as exc:
            Rectangle(1, 2, -3)
        self.assertEqual(str(exc.exception), "x must be >= 0")

    def  test_to_json_string(self):
        "method test_to_json_string"

        r1 = Base.to_json_string(None)
        self.assertEqual(r1, '[]')

    def  test_area(self):
        "method test_area"

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def  test_str_magic(self):
        "method test_str_magic"

        r1 = Rectangle(5, 5, 1)
        self.assertEqual(str(r1), "[Rectangle] (3) 1/0 - 5/5")

    def  test_to_json_string(self):
        "method test_width_heigth"

        r1 = Base.to_json_string(None)
        self.assertEqual(r1, '[]')

        r2 = Base.to_json_string([])
        self.assertEqual(r2, '[]')

        r3 = Base.to_json_string([ { 'id': 12 }])
        self.assertEqual(r3, '[{"id": 12}]')

if __name__ == '__main__':
        unittest.main()
