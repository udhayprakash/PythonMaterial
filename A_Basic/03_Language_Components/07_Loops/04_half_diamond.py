#!/usr/bin/python
"""
Purpose: To display the astrickes in a half-diamond pattern
"""

SIZE = 10
j = 0  # initialization
print 'j=', j
while j < SIZE:  # condition
    j += 1  # increment/decrement
    print '*' * j

print 'j=', j

while j > 0:
    print '*' * j
    j -= 1

print 'j=', j

# implementation with for loop
for j in range(SIZE):  # range(10) = range(0,10,1)
    print '*' * j

for j in range(SIZE, 0, -1):  # range(10,0,-1)
    print '*' * j
