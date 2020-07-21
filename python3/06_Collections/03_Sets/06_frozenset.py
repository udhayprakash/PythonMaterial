#!/usr/bin/python 
"""
Purpose: frozenset
"""
binary_elements = frozenset({'0', '1'})

# binary_elements.add('2')  # AttributeError: 'frozenset' object has no attribute 'add'

students = {'ram', 'rahim', 'robert'}
students.add('ramanaji')

print(f'{binary_elements = }')
print(f'{students        = }')

