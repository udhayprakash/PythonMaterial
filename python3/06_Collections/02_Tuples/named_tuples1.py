#!/usr/bin/python
"""
named tuples provide 
1. access by index - like normal tuples
2. access by keyname - like dictionaries
3. using getattr()
"""
student_details  = ('Nandini', '19', '2541997')


import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

print('type(S)', type(S))
print()
# Access using index
print("The Student age using index is : ")
print(S[1])

# Access using name 
print("The Student name using keyname is : ")
print('S.name', S.name)
print(' S.age',  S.age)
print(S.DOB)

print("hasattr(S, 'DOB')", hasattr(S, 'DOB'))

# Access using getattr()
print("The Student DOB using getattr() is : ")
print("getattr(S, 'DOB')", getattr(S, 'DOB'))

# named tupleis immutable
# print("setattr(S, 'DOB', 76876876)", 
#                  setattr(S, 'DOB', 76876876))

# S['DOB'] =  76876876