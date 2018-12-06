#!/usr/bin/python
"""
Purpose: 
	break     - breaks the complete loop
	continue  - skip the current loop
	pass      - will do nothing. it is like a todo
	sys.exit  - will exit the script execution
"""

print 'importance of break'
i = 0
while i < 10:
    i += 1
    if i == 5:
        break
    print i

print 'importance of continue'
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print i

print 'importance of pass'
i = 0
while i < 10:
    i += 1
    if i == 5:
        pass
    print i

import sys

print 'importance of sys.exit'
i = 0
while i < 10:
    i += 1
    if i == 5:
        sys.exit(0)
    print i

print 'next statement'

# # # implementation with for loop
# # for j in range(size):   # range(10) = range(0,10,1)
# #     print '*'*j

# # for j in range(size,0, -1):   # range(10,0,-1)
# #     print '*'*j
