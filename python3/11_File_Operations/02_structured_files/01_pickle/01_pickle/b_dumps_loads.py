#!/usr/bin/python
"""
Purpose: Pickle file operations

    serialization
        python objects - > flattened content  -- string/file

            dump  -- into a file
            dumps -- into a python string

    De-serialization
        string/file --> unflattened content -> python objects

            load  -- from a file
            loads -- from a python string
"""
import pickle

n1 = (1, 2, 3, 4, 5)

# Python object to pickle string
pickle_str = pickle.dumps(n1)
print(f"pickle_str      :{pickle_str}")

# Pickle string to Python object
retrieved_obj = pickle.loads(pickle_str)
print(f"retrieved_obj   :{retrieved_obj} {type(retrieved_obj)}")
print()
# -------------------------------------------

n1 = {"asd", "cat", "bat", "rat"}

pickle_str = pickle.dumps(n1)
print(f"pickle_str      :{pickle_str}")

retrieved_obj = pickle.loads(pickle_str)
print(f"retrieved_obj   :{retrieved_obj} {type(retrieved_obj)}")
print()
# ---------------------------------------------
n1 = None

pickle_str = pickle.dumps(n1)
print(f"pickle_str      :{pickle_str}")

retrieved_obj = pickle.loads(pickle_str)
print(f"retrieved_obj   :{retrieved_obj} {type(retrieved_obj)}")
print()

# ----------------------------------------------
n1 = False

pickle_str = pickle.dumps(n1)
print(f"pickle_str      :{pickle_str}")

retrieved_obj = pickle.loads(pickle_str)
print(f"retrieved_obj   :{retrieved_obj} {type(retrieved_obj)}")

print()

# ----------------------------------------------
n1 = 212312323123

pickle_str = pickle.dumps(n1)
print(f"pickle_str      :{pickle_str}")

retrieved_obj = pickle.loads(pickle_str)
print(f"retrieved_obj   :{retrieved_obj} {type(retrieved_obj)}")
