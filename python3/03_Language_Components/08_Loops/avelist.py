#!/usr/bin/python
"""
Purpose:
"""

num_list = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    num_list.append(value)

average = sum(num_list) / len(num_list)
print(f'Average:{average}')
