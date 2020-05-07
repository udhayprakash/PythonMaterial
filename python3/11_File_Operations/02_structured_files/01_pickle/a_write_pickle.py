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

.pickle/.pkl
"""
import pickle

favorite_color = {"lion": "yellow", "kitty": "red"}

# Python object to flat string
serialized_string = pickle.dumps(favorite_color)
print(serialized_string)

# Python object to pickle file
with open('first_line.pickle', 'wb') as f:
    pickle.dump(favorite_color, f)
