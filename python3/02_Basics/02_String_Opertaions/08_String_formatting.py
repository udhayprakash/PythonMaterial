#!/usr/bin/python
"""
Purpose: String formatting
        F-strings string formatting
"""

print('f-strings', '='* 20)

name = 'World'
print(f"Hello {name}")
# python operations on data within the f-string 
print(f"Hello {name.upper()}")

value = 123123
print(f'The value is {float(value)}')

NAME='udhay'
AGE=99
SALARY=9999.9999
print(f'''
        Name  :{NAME} , Name  :{NAME}
        Age   :{AGE} 
        Salary:{SALARY}''')