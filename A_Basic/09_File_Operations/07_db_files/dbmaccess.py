#!/usr/bin/env python

import anydbm
import whichdb

# Check the type.
print "Type of DBM file =", whichdb.whichdb('websites')

# Open existing file.
db = anydbm.open('websites', 'w')

# Add another item.
db['www.wrox.com'] = 'Wrox home page'

# Verify the previous item remains.
if db['www.python.org'] != None:
    print 'Found www.python.org'
else:
    print 'Error: Missing item'


# Iterate over the keys. May be slow.
# May use a lot of memory.
for key in db.keys():
    print "Key =",key," value =",db[key]

del db['www.wrox.com']
print "After deleting www.wrox.com, we have:"

for key in db.keys():
    print "Key =",key," value =",db[key]

# Close and save to disk.
db.close()
