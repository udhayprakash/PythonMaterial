#!/usr/bin/python3
"""
Purpose: Temperature Conversions
    - celsius to fahrenheit  
"""
celsius = float(input('Enter temperature in celsius:'))
# print(f'{celsius =}')

farhenheit = (1.8 * celsius) + 32
# print(f'{farhenheit =}')


print(f'''
        celsius     : {round(celsius, 2)}
        farhenheit  : {round(farhenheit, 2)}
''')
