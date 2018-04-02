#!/usr/bin/python
"""
Purpose: To display the astrickes in a half-diamond pattern
"""

size = 10
j=0
print 'j=',j
while j<size:
	print '*'*j
	j+=1

print 'j=',j

while j>0:
	print '*'*j
	j-=1

print 'j=',j

# implementation with for loop
for j in range(size):
    print '*'*j

for j in range(size,0, -1):
    print '*'*j