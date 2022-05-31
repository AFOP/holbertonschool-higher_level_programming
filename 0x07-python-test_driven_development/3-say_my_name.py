#!/usr/bin/python3
""" Say_my_name is:
        write a function that prints My name is first name last name
        first name: the first string
        last name: the second string
        Return: list with the strings """


def say_my_name(first_name, last_name=""):
    """Write a function that prints My name is first name last name
        first name: the first string
        last name: the second string """

    if (first_name is None):
        raise TypeError("first_name must be a string")
    if (last_name is None):
        raise TypeError("last_name must be a string")
    if (type(first_name) != str):
        raise TypeError("first_name must be a string")
    if (type(last_name) != str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
