#!python -u 
"""
Purpose: changing weather from C to F OR F to C
"""

temp = input("please enter the temp, in c or F(default is c): ").lower().strip()

if 'f' in temp:
    mode = 'fahrenheit'
elif 'c' in temp:
    mode = 'celcius'
else:
    mode = 'celcius'


if mode == 'celcius':
    celcius = int(temp.strip('c'))
    Fahrenheit = round((1.8 * celcius) + 32)
else:# farenheit
    Fahrenheit = int(temp.strip('f'))
    celcius = round((Fahrenheit - 32) * 5.0 / 9.0)

print(f'''
        celcius     : {celcius}
        farenheit   : {Fahrenheit}
''')