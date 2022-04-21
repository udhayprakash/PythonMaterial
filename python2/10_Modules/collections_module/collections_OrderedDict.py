from collections import OrderedDict

# regular unsorted dictionary
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# dictionary sorted by key
print OrderedDict(sorted(d.items(), key=lambda t: t[0]))
#OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

# dictionary sorted by value
print OrderedDict(sorted(d.items(), key=lambda t: t[1]))
#OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])

# dictionary sorted by length of the key string
print OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
#OrderedDict([('pear', 1), ('apple', 4), ('orange', 2), ('banana', 3)])

my_dict = OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))

print 'my_dict\n', my_dict

print my_dict.popitem()
print 'after my_dict.popitem()\n', my_dict


print my_dict.popitem(last=False)
print 'after my_dict.popitem()\n', my_dict
