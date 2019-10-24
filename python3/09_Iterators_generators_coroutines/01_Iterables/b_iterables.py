"""
Purpose: Iterating and using enumerate()

"""
my_string = 'Program'

for ech_chr in my_string:
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