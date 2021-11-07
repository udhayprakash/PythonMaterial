#!/usr/bin/python3
"""
Purpose: Iterating and using enumerate()

"""
my_string = 'Program'

count = 0
for ech_chr in my_string:
    print(count, ech_chr)
    count += 1

print()
for ech_chr in enumerate(my_string):
    print(ech_chr)

print()
for loop_index, ech_chr in enumerate(my_string):
    print(f'At loop {loop_index:2}, we found {ech_chr}')

print()
for loop_index, ech_chr in enumerate(my_string, start=0):
    print(f'At loop {loop_index:2}, we found {ech_chr}')

print()
for loop_index, ech_chr in enumerate(my_string, start=4):
    print(f'At loop {loop_index:2}, we found {ech_chr}')

print()
for loop_index, ech_chr in enumerate(my_string, start=-3):
    print(f'At loop {loop_index:2}, we found {ech_chr}')

# for loop_index, ech_chr in enumerate(my_string, start=-3.5):
#     print(f'At loop {loop_index:2}, we found {ech_chr}')
# TypeError: 'float' object cannot be interpreted as an integer
