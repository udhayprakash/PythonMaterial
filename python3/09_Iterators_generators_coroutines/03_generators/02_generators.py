#!/usr/bin/python
"""
Purpose:

Generator objects
    - designed for user-defined functions
    - disposable
    - can't be indexed
    - stores the state
    - used for large data handling
"""
# definition
def foo():  
    print("Start the function!")
    for i in range(3):
        print("before yield", i)
        yield i
        # return i
        print("after yield", i)

    print("end of function ")
    # return None
     

# call 
f = foo() 
print('f', f) 
# print(dir(f))

print(next(f))
print()
print(f.__next__())
print()
print(next(f))
print()
# print(f.__next__())  # StopIteration

try:
    print(next(f))
except StopIteration as ex:
    print('error is ', repr(ex))

print('using loop to get remaining elements')
for i in f:
    print(i)

print("====reinitialize call ")
f = foo()
for i in f:
    print(i)

print("====reinitialize call ")
f = foo()
print(list(f))

print("====reinitialize call ")
f = foo()
print(tuple(f))

print("====reinitialize call ")
f = foo()
print(set(f))

print("====reinitialize call ")
f = foo()
print([i for i in f])
