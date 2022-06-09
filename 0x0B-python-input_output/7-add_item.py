#!/usr/bin/python3
""" Write a script that adds all arguments to a
Python list, and then save them to a file"""

import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

lista = sys.argv[1:]


filename = "add_item.json"
validator = os.path.exists(filename)
if validator is False:
    save_to_json_file(lista, filename)
else:
    x = load_from_json_file(filename)
    for i in lista:
        x.append(i)
    save_to_json_file(x, filename)
