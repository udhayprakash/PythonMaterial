#!/usr/bin/python3
"""
Purpose: Temperature Conversions
    - celsius to fahrenheit  
"""

celsius = float(input('Enter temparature, in celsius:'))
# print(f'{celsius    =}')

farhenheit = (1.8 * celsius) + 32
# print(f'{farhenheit =}')


print(f''' 
        celsius     : {round(celsius, 2)}
        farhenheit  : {round(farhenheit, 2)}
''')

for i in range(0, 9, 1):
    # print(i, round(farhenheit, i))
    print(f'rounding to {i} digits, post decimal, results {round(farhenheit, i):10}')