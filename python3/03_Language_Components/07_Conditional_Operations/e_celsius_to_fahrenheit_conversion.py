#!/usr/bin/python3
"""
Purpose: Temperature Conversions
    - celsius to fahrenheit
"""
celsius = float(input("Enter temperature, in celsius:"))
# print(f'{celsius    = }')

farhenheit = (1.8 * celsius) + 32  # PEMDAS
# print(f'{farhenheit = }')


print(
    f"""
    Celsius     : {celsius:5.2}
    Fahrenheit  : {farhenheit:5.2}
"""
)

print(
    f"""
    {celsius    = : 5.2}
    {farhenheit = : 5.2}
"""
)

print(
    f"""
    Celsius     : {round(celsius, 2)}
    Fahrenheit  : {round(farhenheit, 2)}
"""
)

import math

farhenheit = math.pi

for i in range(0, 9, 1):
    # print(i, round(farhenheit, i))
    print(f"rounding to {i} digits, post decimal, results {round(farhenheit, i):10}")
