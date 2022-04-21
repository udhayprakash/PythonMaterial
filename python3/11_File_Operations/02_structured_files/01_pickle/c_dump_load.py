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

data = (
    123,
    123.32,
    -0.000098,
    None,
    True,
    False,
    "Python",
    [1, 2],
    (23,),
    {23, 23},
    {"a": 1},
)

with open("serialized_data.pkl", "wb") as f:
    pickle.dump(data, f)
    f.close()

with open("serialized_data.pkl", "rb") as g:
    retrieved_data = pickle.load(g)
    print(f"retrieved_data: {retrieved_data} {type(retrieved_data)}")

assert data == retrieved_data

# ---------------------------
data = True

with open("serialized_data.pkl", "wb") as f:
    pickle.dump(data, f)
    f.close()

with open("serialized_data.pkl", "rb") as g:
    retrieved_data = pickle.load(g)
    print(f"retrieved_data: {retrieved_data} {type(retrieved_data)}")

# cpython - it is c implementation of python
# Pickle and cpickle has their importance in interfacing with c and C++.
# in python 2

# In python 3, cpickle is renamed as pickle
