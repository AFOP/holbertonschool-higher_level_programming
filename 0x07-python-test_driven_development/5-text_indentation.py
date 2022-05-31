#!/usr/bin/python3
""" text_indentation:
        function that prints a text with 2 new lines
        after each of these characters: ., ? and :
        text: is the string
        Return: Nothing """


def text_indentation(text):
    """ Write a function that prints a text with
        2 new lines after each of these characters: ., ? and :
        text: is the string """

    if text is None:
        raise TypeError("text must be a string")
    if type(text) != str:
        raise TypeError("text must be a string")
    no_spaces = text.strip()
    for x in no_spaces:
        x = x.strip()
        print(x, end="")
        if (x == "." or x == "?" or x == ":"):
            print()
            print()
