#!/usr/bin/python
"""
Purpose: Named Tuple ops 
"""
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')

# Assignments
hen = Animal('hen', '2', 'bird')
#              0     1     2
print(hen)

hen = Animal(name='hen', age='2', type='bird')
print(hen)

hen = Animal(age='2', name='hen', type='bird')
print(hen)  
# NOTE: Even if the order of values are changes, it can understand

# To get the field names 
print(f'{hen._fields =}')

# Accessing values 
print()
print('Access By position:', hen[2])
print('Access By key name:', hen.type)

# Converting to dictionary 
print(f'{hen._asdict() =}')
