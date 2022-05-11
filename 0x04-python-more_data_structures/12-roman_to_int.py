#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string and type(roman_string) == 'string':
        return 0
    if not isinstance(roman_string, str):
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    valores = []
    sum = 0
    for x in roman_string:
        if x in roman:
            valores.append(roman.get(x))
    if len(valores) > 1:
        j = 1
        for i in range(len(valores)):
            if j == len(valores):
                break
            elif valores[j] <= valores[i]:
                sum += valores[i]
            else:
                sum -= valores[i]
            j += 1
        sum += valores[i]
    else:
        sum += valores[0]
    return sum
