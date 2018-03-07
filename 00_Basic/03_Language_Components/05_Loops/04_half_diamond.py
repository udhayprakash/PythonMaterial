#!/usr/bin/python
"""
Purpose: Half Diamond
"""

for i in xrange(0,9, 1):
    print i * '*'
for j in xrange(9, 0, -1):
    print j * '*'


i = 0
while i < 9:
    print '*' * i
    i += 1
    
#print 'i=', i
while i >0:
    print '*' * i
    i -= 1
print 'i=', i
