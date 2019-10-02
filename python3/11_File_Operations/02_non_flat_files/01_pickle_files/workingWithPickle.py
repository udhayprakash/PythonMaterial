#!/usr/bin/python
'''
Purpose: Working with Pickle files
    pickling

    serilization 
        python objects - > flattened content  -- string/file
        
            dump  -- into a file 
            dumps -- into a python string 

    De-serilization 
        string/file --> flattened content -> python objects 

            load  -- from a file 
            loads -- from a python string 

'''
import pickle

# Serialization
students = ['Michel', 'John', 'Udhay', 'Ana', 123]

f = open('BelgiumStudents.pkl', 'wb')  # 'wb' instead 'w' for binary file
pickle.dump(students, f, -1)  # -1 specifies highest binary protocol
f.flush()
f.close()

# Deserialization
g = open('BelgiumStudents.pkl', 'rb')
myStudents = pickle.load(g)
print("myStudents are ", myStudents)
g.close()

# cpython - it is c implementation of python
# Pickle and cpickle has their importance in interfacing with c and C++.
