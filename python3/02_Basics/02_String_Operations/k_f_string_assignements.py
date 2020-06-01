#!/usr/bin/python
"""
Purpose: F-String Assignments 

        Introduced in python 3.8
"""
language = 'Python'
print(f'language = {language}')
print(f'{language}')
print(f'{language =}')

num = 123
print(f'num={num}')
print(f'{num=}')

print(f'Number={num}')
# print(f'{Number=}')
# NameError: name 'Number' is not defined

print()
print(f'{num     = }')
print(f'{num     = }')
print(f'{num * 3 = }')
print(f'{num / 3 = }')
print(f'{num % 3 = }')
