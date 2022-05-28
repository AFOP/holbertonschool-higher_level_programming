#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print("case 1: ", add_integer(None))
print("case 2: ", add_integer(-2))
print("case 3: ", add_integer(100.3, 100.3))
print("case 4: ", add_integer(1, 2, 3))
try:
    print("case 6: ", add_integer(2, "&"))
except Exception as e:
    print(e)
try:
    print("case 7: ", add_integer(2, "&", "     "))
except Exception as e:
    print(e)
try:
    print("case 8: ", add_integer({2:3}))
except Exception as e:
    print(e)
