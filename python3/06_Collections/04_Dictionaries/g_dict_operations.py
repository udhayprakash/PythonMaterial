#!/usr/bin/python3
"""
Purpose: Dictionaries
"""
animal = {'name': 'zebra', 'continent': ('Africa', 'Asia')}
print(animal)

# replicas - To get the keys of existing dictionary to new dict
animal_schema = {}
animal_schema = animal_schema.fromkeys(animal)
print(animal_schema)
# NOTE: Default value is None


animal_schema = animal_schema.fromkeys(animal, None)
print(animal_schema)

animal_schema = animal_schema.fromkeys(animal, 'None')
print(animal_schema)

animal_schema = animal_schema.fromkeys(animal, '')
print(animal_schema)

# To flush the content in the dictionary
print()
print(f'{id(animal) = }')
animal.clear()  # will flush the key-value pairs in dict
print(f'After dict.clear(), {animal =}')
print(f'{id(animal) = }')
