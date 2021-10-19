#!/usr/bin/python
"""
Purpose: Dictionary operations
"""
from pprint import pprint

employee = {
    'name': 'Saurav Ganguly',
    'status': 'retired',
    'salary': 12_222_213,
    'strike_rate': 85/100,
}

# Indexing in Dictionaries
print('Employee Name  :', employee['name'])
print('Employee Status:', employee['status'])

try:
    employee['no_of_centuries']
except KeyError as ex:
    print(f'No such key :{str(ex)}')


# Dictionaries are mutable
print()
print(f'Before change: {id(employee) = }')

# Updating value for existing key
employee['status'] = 'rejoined'
print('Employee Status:', employee['status'])
print(f'After change : {id(employee) = }')

# To add a new key
employee['no_of_centuries'] = 345
print(employee)
pprint(employee)
print()

# Difference ways of indexing
# Question: dict['key'] vs dict.get() vs dict.setdefault

print(f"{employee['strike_rate'] =}")

try:
    print(f"{employee['no_of_catches'] =}")
except KeyError as ex:
    print(f'No such key :{str(ex)}')


print()
print(f"{employee.get('strike_rate')                    =}")
print(f"{employee.get('no_of_catches')                  =}")
# NOTE: dict.get() - returns None if key is not present
print(f"{employee.get('no_of_catches', None)            =}")
print(f"{employee.get('no_of_catches', 'No such key')   =}")
print(f"{employee.get('no_of_catches', 234)             =}")

pprint(employee)
print()

print(f"{employee.setdefault('strike_rate')        =}")
print(f"{employee.setdefault('no_of_catches')      =}")  # default is None
pprint(employee)
print()

print(f"{employee.setdefault('no_of_catches', 234) =}")
# As this key is present now, default values is not taken
pprint(employee)
print()

print(f"{employee.setdefault('ODI_matches_played', 155) =}")
pprint(employee)
print()


#  in - operator - membership check
print(f"{'no_of_catches' in employee            =}")
print(f"{employee.__contains__('strike_rate')   =}")

print(f"{'no_of_wickets' in employee            =}")
print(f"{employee.__contains__('no_of_wickets') =}")

if 'no_of_catches' in employee:
    print("no_of_catches:", employee['no_of_catches'])
else:
    print('No such key')
