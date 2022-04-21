#!/usr/bin/python

# built-in
# print is the simplest example of variadic function
print((12))
print((12, '34', 'three'))

# User defined
def addition(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(addition(9,8,7,6,5,4))
