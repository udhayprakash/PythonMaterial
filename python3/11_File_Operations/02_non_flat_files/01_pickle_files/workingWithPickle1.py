#!/usr/bin/python

import pickle
'''
Purpose: Working with Pickle strings
    pickling

files - dump & load
string - dumps & loads
'''
# Serialization
students = ['Michel', 'John', 'Udhay', 'An', 123]

my_pickle_string =  pickle.dumps(students)
print("my_pickle_string", my_pickle_string)
print(type(my_pickle_string))

# Deserialization
myStudents = pickle.loads(my_pickle_string)
print(f"myStudents are {myStudents}")


# cpython - it is c implementation of python
# Pickle and cpickle has their importance in interfacing with c and C++.