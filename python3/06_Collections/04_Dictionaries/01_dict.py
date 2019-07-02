#!/usr/bin/python
"""
Purpose: dictionary demo

1. keys are unique; 
2. keys should be immutables only
    immutables 
        string, tuple, int, long, float, bool
    mutables
        bytearray string, list, set, dict
3. indexing based on keys 
4. They were unordered

"""
empty_dict = {}
print(empty_dict, type(empty_dict))

empty_dict = dict()
print(empty_dict, type(empty_dict))

empty_set = set()
print(empty_set, type(empty_set))

other_set= {12, 34}
print(type(other_set))

other_dict = {12:34}
print(type(other_dict))

# in python2, dicts doesn't retain the assigned order. 
# whereas in python3, they wil
mydict = {
    'name': ['udhay', 'prakash'],
    'blog': 'udhayprakash.blogspot.in',
    0.000001 : other_dict,
     99 : ('age', 'price'),
    ('Dr', 'Mr'): 'titles',
    'name': 'somebody'
}

print(mydict)
print(type(mydict))

from pprint import pprint
# print(dir(pprint))
# help(pprint)

pprint(mydict, indent=2, width=2)

########################################
print()
print('name' in mydict)
print("mydict['name']:", mydict['name'])

#  dictionary is a mutable object 
mydict['name'] = 'shyam'
print("mydict['name']:", mydict['name'])

print('name1' in mydict)
# print("mydict['name1']:", mydict['name1'])#  KeyError: 'name1'

print("mydict.get('name1')                  :", mydict.get('name1'))
print("mydict.get('name1', None)            :", mydict.get('name1', None))
print("mydict.get('name1', 'key not present'):", mydict.get('name1', 'key not present'))
print()
print(mydict)
print(mydict.setdefault('name1', 'Key not present'))
print(mydict)
print(mydict.setdefault('name', 'Key not present'))
print(mydict)

mydict['company'] = 'abc infotech'
print('mydict', mydict)

####################################
print(dir(mydict))
print('===============')
print(mydict.popitem())  # deletes some key:value in random 
print(mydict)

print(mydict.popitem())
print(mydict)

print(mydict.pop('name'))  # deletes specific mentioned key:value
print(mydict)
print()
del mydict[('Dr', 'Mr')]   # deletes specific mentioned key:value
print(mydict)


print('-'*50)
print('mydict.keys()', mydict.keys())
print('mydict.values()', list(mydict.values()))
print('mydict.items()', list(mydict.items()))
print('-'*50)
# print('mydict.iterkeys()', mydict.keys())
# print('mydict.itervalues()', mydict.values())
# print('mydict.iteritems()', mydict.items())

replica_dict = {}
replica_dict= replica_dict.fromkeys(mydict, '')
print('\n\nreplica_dict', replica_dict)

replica_dict['b'] = 'bbb'

# print(mydict + replica_dict) # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

replica_dict.update({'a':12, 'blog': 'udhay'})
print('replica_dict', replica_dict)

mydict.clear()
print(mydict)

del mydict
# print(mydict) #NameError: name 'mydict' is not defined
