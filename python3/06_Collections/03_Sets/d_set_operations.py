#!/usr/bin/python3
"""
Purpose: Set Operations 
    - Venn Diagrams

"""
rainbow = {'red', 'orange', 'yellow', 'green',
           'blue', 'indigo', 'violet'}

traffic_lights = {'red', 'yellow', 'green', 'white'}

print(f'{rainbow =}')
print(f'{traffic_lights =}')


print()
print(f'{traffic_lights.issubset(rainbow)   =}')
print(f'{rainbow.issuperset(traffic_lights) =}')


alphabets = {'a', 'b', 'c'}
print(f'{alphabets.issubset(rainbow)   =}')
print(f'{rainbow.issuperset(alphabets) =}')

print()
print(f'{traffic_lights.isdisjoint(rainbow)   =}')  # False
# {'green', 'red', 'yellow'}
print(f'{traffic_lights.intersection(rainbow) =}')

print()
print(f'{alphabets.isdisjoint(rainbow)        =}')  # True
print(f'{alphabets.intersection(rainbow)      =}')  # set()


# Set concatenation is not possible
# rainbow + traffic_lights  # TypeError: unsupported operand type(s) for +: 'set' and 'set'

# Set difference
# - from first set, remove common elements between both sets
print()
print(f'{rainbow - traffic_lights =}')
print(f'{traffic_lights - rainbow =}')


# To get the all elements between both sets
print()
print(f'{rainbow.union(traffic_lights) =}')
print(f'{traffic_lights.union(rainbow) =}')

# To get the common elements between both sets
print()
print(f'{rainbow.intersection(traffic_lights) =}')
print(f'{traffic_lights.intersection(rainbow) =}')


# Symmetic Difference
#   - To get elements of both sets, which are not common
#   - For sets A, B, symmetic_difference is (A U B) - (A intersection B)
print()
print(f'{rainbow.symmetric_difference(traffic_lights) =}')
print(f'{traffic_lights.symmetric_difference(rainbow) =}')
