#!/usr/bin/python

def simple_gen():
    yield "Hello"
    yield "World"
 
 
gen = simple_gen()
print((next(gen)))
print((next(gen)))


def count(n):
    print("Stating to count!")
    i = 0
    while i < n:
        yield i
        # print i
        i += 1
    print('$', i)
    # return i 


# PEP8 strongly discourages usage of yield and retun, in same function


c = count(9)
print(c)

print('c.next() ', next(c))

print('looping')
for val in c:
    print(val)
