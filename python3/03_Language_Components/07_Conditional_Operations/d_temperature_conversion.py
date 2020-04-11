#!/usr/bin/python
"""
Purpose: Temperature Conversions
    - celsius to fahrenheit , or vice versa

round(number, no_of_digits_to_round_post_decimal)
"""
__name__ = 'Author'

temperature = input('Enter the temperature, followed by C or F:').upper()
# print(type(temperature), temperature)

if 'C' in temperature:
    celsius = float(temperature.strip('C '))
    fahrenheit = round((1.8 * celsius) + 32, 2)
elif 'F' in temperature:
    fahrenheit = float(temperature.strip('F '))
    celsius = round((fahrenheit - 32) * 5.0 / 9.0, 2)
else:
    # Default is celsius
    celsius = float(temperature.strip('C '))
    fahrenheit = round((1.8 * celsius) + 32, 2)

print(f'''
        celsius     : {celsius}
        fahrenheit  : {fahrenheit}
''')
