#!/usr/bin/python
"""
Purpose: dictionary demo

1. keys are unique; 
2. keys should be immutables only 
3. indexing based on keys 
4. They were unordered

"""


from pprint import pprint 

mydict = {}

print type(mydict)

other_set= {12, 34}
print type(other_set)

other_dict = {12:34}
print type(other_dict)


mydict = {
    'name': ['udhay', 'prakash'],
    'blog': 'udhayprakash.blogspot.in', 
    0.000001 : other_dict,
     99 : ('age', 'price'),
    ('Dr', 'Mr'): 'titles'
}

print mydict
print type(mydict)

pprint(mydict)

print 'mydict.keys()', mydict.keys()
print 'mydict.values()', mydict.values()
print 'mydict.items()', mydict.items()

########################################

print "mydict['name']:", mydict['name']

#  dictionary is a mutable object 
mydict['name'] = 'shyam'

print "mydict['name']:", mydict.get('names')
mydict['company'] = 'abc infotech'

print 'mydict', mydict

#############################
pprint(mydict.keys() + mydict.values())
print(mydict.keys() + mydict.values())

####################################
print dir(mydict)
print '==============='
print mydict.popitem()
print mydict

print mydict.popitem()
print mydict


print mydict.pop('name')
print mydict


print mydict.clear()
print mydict
