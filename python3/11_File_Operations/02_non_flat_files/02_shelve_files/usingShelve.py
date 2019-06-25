#!/usr/bin/python

#usingShelve.py

'''
    Purpose: Demonstrating the purpose of shelve
'''
import shelve

# creating a new shelve file
s = shelve.open('michelShelve.db')
try:
    s['key1'] = { 'int': 10, 'float':9.5, 'string':'Sample data' }
except Exception as  ex:
    print(ex)
finally:
    s.close()

# To access the data again, open the shelve and use it like a dictionary
s = shelve.open('michelShelve.db')
try:
    existing = s['key1']
except Exception as ex:
    print(ex)
finally:
    s.close()

print(existing)

# shelve doesn't allow multiple applications writing to the same database at the same time.
# So, it is best practice to open the database in read-only mode, in general.

s = shelve.open('michelShelve.db', flag='r')
try:
    existing = s['key1']
finally:
    s.close()

print(existing)


# By defaults, shelve do not track modifications to volatile objects.

s = shelve.open('michelShelve.db')
try:
    print(s['key1'])
    s['key1']['new_value'] = 'this was not here before'
finally:
    s.close()

s = shelve.open('michelShelve.db', writeback=True)
try:
    print(s['key1'])   # modifications are not reflected
finally:
    s.close()

# To automatically catch the changes, open the shelve with writeback enabled
s = shelve.open('michelShelve.db', writeback=True)
try:
    print(s['key1'])
    s['key1']['new_value'] = 'this was not here before'
    print(s['key1'])
finally:
    s.close()

s = shelve.open('michelShelve.db', writeback=True)
try:
    print(s['key1'])
finally:
    s.close()

# Note: Shelve must not be opened with writeback enabled, unless it is essential