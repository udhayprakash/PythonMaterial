#!/usr/bin/python
"""
Purpose: Temperature Conversions
    - celsius to fahrenheit  

round(number, no_of_digits_to_round_post_decimal)
"""
__name__ = 'Author'

celsius = float(input('Enter temperature in celsius:'))

farhenheit = (1.8 * celsius) + 32
farhenheit = round(farhenheit, 2)

print(f'''
        celsius     : {celsius}
        farhenheit  : {farhenheit}
''')
