#!/usr/bin/python
"""
Purpose: 
	break     - breaks the complete loop
	continue  - skip the current loop
	pass      - will do nothing. it is like a todo
"""

print 'importance of break'
i = 0
while i <10:
	i += 1
	if i == 5:
		break
	print i

print 'importance of continue'
i = 0
while i <10:
	i += 1
	if i == 5:
		continue
	print i

print 'importance of pass'
i = 0
while i <10:
	i += 1
	if i == 5:
		pass
	print i


# # implementation with for loop
# for j in range(size):   # range(10) = range(0,10,1)
#     print '*'*j

# for j in range(size,0, -1):   # range(10,0,-1)
#     print '*'*j