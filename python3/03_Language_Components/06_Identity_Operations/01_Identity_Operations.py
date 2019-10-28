#!/usr/bin/python
"""
Purpose: Demo of Identity Operations


is 

is not 

== - value level equivalence ( value and type) check
is - object level equivalence (address location, value and type) check

Object
    - value(s)
    - type(s)
    - address location where it is stored - id()

Dual Memory management Strategy
integers: -5 to 256
"""

print('4 == 4  ', 4 == 4)  # True
print('4 == "4"', 4 == "4")  # False
print('4 is 4  ', 4 is 4)
print()

a = 100
b = 200

print('a=', a, 'b=', b)

print('a == b ', a == b)
print('a is b ', a is b)
print('id(a)= ', id(a), 'id(b)', id(b))  # id(a)= 4368732 id(b) 4368732
print()

a = 200
print('a=     ', a, 'b=', b)
print('id(a)= ', id(a), 'id(b)', id(b))  # id(a)= 4368732 id(b) 4368732
print('a == b ', a == b)
print('a is b ', a is b)
print()

m = 300
n = 300
print('m=', m, 'n=', n)
print('id(m)= ', id(m), 'id(n)', id(n))  # id(m)= 36645972 id(n) 36645972
print('m == n ', m == n)
print('m is n ', m is n)
print()

# a = 255
# b = 255
# print('a=', a, 'b=', b)
# print('id(a)=', id(a), 'id(b)', id(b))  # id(a)= 4370056 id(b) 4370056
# print('a == b ', a == b)
# print('a is b ', a is b)

# # Dual memory management strategy 
# # -------------------------------------
# # if each object created in independent line,
# # -5- 256 --- no new object created
# # > 256 ---  new object created for every assignment 
# # else 
# # no new object get created on new variable assignment for the same value 

# """
# >>> m = 300
# >>> n = 300
# >>> print 'm=', m, 'n=', n
# m= 300 n= 300
# >>> print 'id(m)=', id(m), 'id(n)', id(n)   # id(a)= 4370044 id(b) 4370044
# id(m)= 36646032 id(n) 36646008
# >>> print 'm == n ', m == n
# m == n  True
# >>> print 'm is n ', m is n
# m is n  False

# >>> m = 300; n = 300
# >>> print 'm=', m, 'n=', n
# m= 300 n= 300
# >>> print 'id(m)=', id(m), 'id(n)', id(n)   # id(a)= 4370044 id(b) 4370044
# id(m)= 36645972 id(n) 36645972
# >>> print 'm == n ', m == n
# m == n  True
# >>> print 'm is n ', m is n
# m is n  True
# """

# p = 900
# q = 323232
# print('p=', p, 'q=', q)

# print(p is q)
# print('id(p)=', id(p), 'id(q)=', id(q))
# # print p not is q  # SyntaxError: invalid syntax
# print(p is not q)
# print(p != q)


'''
>>> v1 = 'udhay'
>>> v2 = 'udhay'
>>>
>>> id(v1)
35989168
>>> id(v2)
35989168
>>> v2 = 'udhaykjkjkasdkasjdkjasdhkjsahkdjhksjdksajdkdskjashkjdkjashkdjaskjdhkjassssskkjhkjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj'
>>> v1 = 'udhaykjkjkasdkasjdkjasdhkjsahkdjhksjdksajdkdskjashkjdkjashkdjaskjdhkjassssskkjhkjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj'
>>>
>>> v1 is v2
True
'''
