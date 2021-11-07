#!/usr/bin/python3
"""
Purpose: Generator objects
    - designed for user-defined functions
    - disposable
    - can't be indexed
    - stores the state
    - used for large data handling
    - State suspension and on-demand computation
"""


def foo():
    print("Start the function!")
    for i in range(3):
        print("\tbefore yield", i)
        # return i
        yield i
        print("\tafter yield", i)

    print("end of function ")
    # return None


# call
f = foo()
print('f', f)
print(dir(f))
# ['__class__', '__del__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
#  '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__name__', '__ne__', '__new__',
#  '__next__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
#  '__subclasshook__',
#
#  'close', 'gi_code', 'gi_frame', 'gi_running', 'gi_yieldfrom', 'send', 'throw']


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

print('\nusing loop to get remaining elements')
for i in f:
    print(i)

print("\n====reinitialize call ")
f = foo()
for i in f:
    print(i)

print("\n====reinitialize call ")
f = foo()
print(list(f))

print("\n====reinitialize call ")
f = foo()
print(tuple(f))

print("\n====reinitialize call ")
f = foo()
print(set(f))

print("\n====reinitialize call ")
f = foo()
print([i for i in f])

print("\n====reinitialize call ")
f = foo()
print(str(f))
