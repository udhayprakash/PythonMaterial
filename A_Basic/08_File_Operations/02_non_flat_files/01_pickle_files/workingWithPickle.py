#!/usr/bin/python

import pickle
'''
    Purpose: Working with Pickle files
    pickling

    serilization 
        python objects - > flattened content  -- string/file
        
            dump  -- into a file 
            dumps -- into a python string 

    De-serilization 
        flattened content -> python objects 

            load  -- from a file 
            loads -- from a python string 


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