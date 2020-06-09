#!/usr/bin/python
"""
Purpose: Tuple attributes
"""
mytuple = (12, 5, 6, 8, (5,))
print(dir(mytuple))

print()
print("len(mytuple)           =", len(mytuple))
print("mytuple.__len__()      =", mytuple.__len__())
assert len(mytuple) == mytuple.__len__()

print()
print("str(mytuple)           =", str(mytuple))
print("type(str(mytuple))     =", type(str(mytuple)))
print("mytuple.__str__()      =", mytuple.__str__())
print("type(mytuple.__str__())=", type(mytuple.__str__()))
assert str(mytuple) == mytuple.__str__()

# Tuple repetition operation - original object not modified
print()
print("mytuple * 3            =", mytuple * 3)
print('mytuple                =', mytuple)
print("mytuple.__mul__(3)     =", mytuple.__mul__(3))
print('mytuple                =', mytuple)

print('\n Tuple Attributes excluding dunder methods')
for each_attribute in dir(mytuple):
    if not each_attribute.startswith('__'):
        print(each_attribute)

print('mytuple                =', mytuple)
print('mytuple.count(5)       =', mytuple.count(5))

mytuple = (12, 5, 6, 8, (5))
#          0   1  2  3   4
print('mytuple                =', mytuple)
print('mytuple.count(5)       =', mytuple.count(5))

print()
print('mytuple.index(8)       =', mytuple.index(8))
print('mytuple.index(5)       =', mytuple.index(5))

try:
    print('mytuple.index(55)      =', mytuple.index(55))
except ValueError as ex: 
    print(ex)