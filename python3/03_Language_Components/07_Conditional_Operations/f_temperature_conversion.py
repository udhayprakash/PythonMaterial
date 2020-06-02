#!/usr/bin/python
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
temperature = input('Enter the temperature, followed by C or F:').upper()

if 'C' in temperature:
    celsius = float(temperature.strip('C'))
    fahrenheit = round((1.8 * celsius) + 32, 2)
elif 'F' in temperature:
    fahrenheit = float(temperature.strip('F'))
    celsius = round((fahrenheit - 32) * 5.0 / 9.0, 2)
else:
    # Default is celsius
    celsius = float(temperature.strip('C '))
    fahrenheit = round((1.8 * celsius) + 32, 2)
    
print(f'''
        celsius     : {celsius}
        fahrenheit  : {fahrenheit}
''')