#!/usr/bin/python
"""
Purpose: dictionary demo

1. keys are unique; 
2. keys should be immutables only 
3. indexing based on keys 
4. They were unordered

"""


from pprint import pprint 

mydict = dict() # {}

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
    ('Dr', 'Mr'): 'titles',
    'name': 'somebody'
}

print mydict
print type(mydict)

pprint(mydict)

# ########################################
print
print mydict.has_key('name')
print "mydict['name']:", mydict['name']

#  dictionary is a mutable object 
mydict['name'] = 'shyam'
print mydict.has_key('name1')

print "mydict.get('name1'):", mydict.get('name1', 'key not present')
print mydict
print mydict.setdefault('name1', 'Key not present')
print mydict
print mydict.setdefault('name', 'Key not present')
print mydict

mydict['company'] = 'abc infotech'
print 'mydict', mydict

# #############################
# pprint(mydict.keys() + mydict.values())
# print(mydict.keys() + mydict.values())

# # ####################################
print dir(mydict)
print '==============='
print mydict.popitem()
print mydict

print mydict.popitem()
print mydict


print mydict.pop('name')
print mydict
print
del mydict['company']
print mydict


print '-'*50
print 'mydict.keys()', mydict.keys()
print 'mydict.values()', mydict.values()
print 'mydict.items()', mydict.items()
print '-'*50
print 'mydict.iterkeys()', mydict.iterkeys()
print 'mydict.itervalues()', mydict.itervalues()
print 'mydict.iteritems()', mydict.iteritems()

replica_dict = {}
replica_dict= replica_dict.fromkeys(mydict, '')
print 'replica_dict', replica_dict


replica_dict.update({'a':12, 'name1': 'udhay'})
print 'replica_dict', replica_dict


mydict.clear()
print mydict

del mydict
# print mydict #NameError: name 'mydict' is not defined
