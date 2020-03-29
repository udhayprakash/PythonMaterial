"""

files 
    load  -- file to python object 
    dump  --- python object to file 

strings
    loads  --- string to python object 
    dumps  --- python object to string 

"""
import json

my_dict = {'a': 1, "b": 2}

print(json.dumps(my_dict))

my_tuple = (None, True, 0, -0.004, [1, 2], (4,), "tom", 'cruise')

print(json.dumps(my_tuple))

fh = open('test.json', 'w')
json.dump(my_tuple, fh)

gh = open('test.json', 'r')
# print(json.load(gh))
data = gh.read()
# print(json.loads(data, 'utf-8'))

# Default encoding scheme 
#     python 2 - ASCII
#     python 3 - UTF-8

import ast

print((ast.literal_eval(data)))
