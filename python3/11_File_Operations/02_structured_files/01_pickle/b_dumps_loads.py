#!/usr/bin/python
"""
Purpose: Pickle file operations

    serialization
        python objects - > flattened content  -- string/file

            dump  -- into a file
            dumps -- into a python string

    De-serialization
        string/file --> flattened content -> python objects

            load  -- from a file
            loads -- from a python string
"""
import pickle

n1 = (1, 2, 3, 4, 5)

pickle_str = pickle.dumps(n1)
print(f'pickle_str      :{pickle_str}')

retrieved_obj = pickle.loads(pickle_str)
print(f'retrieved_obj   :{retrieved_obj} {type(retrieved_obj)}')


n1 = {'asd', 'cat', 'bat', 'rat'}

pickle_str = pickle.dumps(n1)
print(f'pickle_str      :{pickle_str}')

retrieved_obj = pickle.loads(pickle_str)
print(f'retrieved_obj   :{retrieved_obj} {type(retrieved_obj)}')


n1 = None

pickle_str = pickle.dumps(n1)
print(f'pickle_str      :{pickle_str}')

retrieved_obj = pickle.loads(pickle_str)
print(f'retrieved_obj   :{retrieved_obj} {type(retrieved_obj)}')


n1 = False

pickle_str = pickle.dumps(n1)
print(f'pickle_str      :{pickle_str}')

retrieved_obj = pickle.loads(pickle_str)
print(f'retrieved_obj   :{retrieved_obj} {type(retrieved_obj)}')
