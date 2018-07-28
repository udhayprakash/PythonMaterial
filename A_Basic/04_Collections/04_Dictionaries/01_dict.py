from pprint import pprint 

mydict = {}


mydict = {
    'name': 'udhay',
    'blog': 'udhayprakash.blogspot.in', 
    'age': 99, 
    'titles': ('Dr', 'Mr')
}

# print mydict
# print type(mydict)
print 'mydict.keys()', mydict.keys()
print 'mydict.values()', mydict.values()


print "mydict['name']:", mydict['name']

mydict['name'] = 'shyam'

print "mydict['name']:", mydict['name']
mydict['company'] = 'abc infotech'

print 'mydict', mydict

print '========================================'
print '='*20

pprint(mydict)

































