#!/usr/bin/python
"""
named tuples provide 
1. access by index - like normal tuples
2. access by keyname - like dictionaries
3. using getattr()
"""
import collections

# Declaring namedtuple()
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# Access using index
print "The Student age using index is : "
print S[1]

# Access using name 
print "The Student name using keyname is : "
print S.name
print S.age
print S.DOB

# Access using getattr()
print "The Student DOB using getattr() is : "
print getattr(S, 'DOB')
