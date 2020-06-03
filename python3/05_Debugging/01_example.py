#!/usr/bin/python
"""
Purpose: Debugging 
"""
import pdb

val_1 = int(input('Enter val_1      :'))
val_2 = int(input('Enter val_2      :'))

# Place below line from where you want to debug
pdb.set_trace()

# Multiplication
result = val_1 * val_2  # val_1 + val_2
print(f'Multiplication   :{result}')
