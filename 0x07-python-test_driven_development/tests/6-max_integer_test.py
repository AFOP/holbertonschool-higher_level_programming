#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class for unittest of max_integer program"""

    def test_MaxInteger(self):
        """Testing function MaxInteger"""

        test_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(test_list), 4)
        test_list = [1.6, 1000, 3, 4]
        self.assertEqual(max_integer(test_list), 1000)
        test_list = [1, 1, 1, 1]
        self.assertEqual(max_integer(test_list), 1)
        test_list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(test_list), -1)
        test_list = ["a", "b", "c", "d"]
        self.assertEqual(max_integer(test_list), "d")
    
    def test_Values(self):
        """Make sure value errors are raised when necesary"""

        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, ["a", -2, -3, -4])
        self.assertRaises(TypeError, max_integer, [[-1, -2, -3, -4], [1, 2], -3, -4])
        self.assertRaises(TypeError, max_integer, ["andres", -2, -3, -4])
        self.assertRaises(TypeError, max_integer, ["&", -2, -3, -4])
