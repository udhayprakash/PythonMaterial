#!/usr/bin/python3
"""
Purpose: Temperature Conversions
    - celsius to fahrenheit , or vice versa


user input : 23c
output     : xF

user input : 23F
output     : xC

23c, 23C, 23F, 23f
23C, 23F
23 C
23C 
"""
temperature = input(
    'Enter the temperature, followed by C or F:').upper()

# Method 1
if 'C' in temperature:
    celsius = float(temperature.strip('C '))
    fahrenheit = (1.8 * celsius) + 32
elif 'F' in temperature:
    fahrenheit = float(temperature.strip('F '))
    celsius = (fahrenheit - 32) * 5.0 / 9.0
else:
    # Default is celsius
    celsius = float(temperature.strip('C '))
    fahrenheit = (1.8 * celsius) + 32


print(f'''
        celsius     : {round(celsius, 2)}
        fahrenheit  : {round(fahrenheit, 2)}
''')

# Method 2 
if 'F' in temperature:
    fahrenheit = float(temperature.strip('F '))
    celsius = (fahrenheit - 32) * 5.0 / 9.0
else:
    # Default is celsius
    celsius = float(temperature.strip('C '))
    fahrenheit = (1.8 * celsius) + 32

print(f'''
        celsius     : {round(celsius, 2)}
        fahrenheit  : {round(fahrenheit, 2)}
''')
