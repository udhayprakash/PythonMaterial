"""

files 
    load  -- file to pythn object 
    dump  --- python object to file 

strings
    loads  --- string to python object 
    dumps  --- pythn object to string 

"""
import json 

my_dict = {'a':1, 'b':2}

print json.dumps(my_dict)

my_tuple = (None, True, 0, -0.004, [1,2],  (4,), "tom", 'cruise')

print json.dumps(my_tuple)

fh = open('test.json', 'wb')
json.dump(my_tuple, fh)

gh = open('test.json', 'rb')

json.load()