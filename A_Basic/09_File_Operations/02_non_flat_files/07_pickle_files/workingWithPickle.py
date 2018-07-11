#!/usr/bin/python

import pickle
'''
    Purpose: Working with Pickle files
    pickling

'''
# Serialization
students = ['Michel', 'John', 'Udhay', 'An', 123]

f = open('BelgiumStudents.pkl', 'ab+')
pickle.dump(students, f)
f.flush()

f.close()

# Deserialization
g = open('BelgiumStudents.pkl', 'rb')
myStudents = pickle.load(g)
print "myStudents are ", myStudents
g.close()


# cpython - it is c implementation of python
# Pickle and cpickle has their importance in interfacing with c and C++.