#!/usr/bin/python
"""
Purpose: Identity Operations

    Object
        - value(s)
        - type(s)
        - address location where it is stored - id()


    =  Assignment operator

    == Value-level Equivalence  -  ( value and type) check
    is object-level Equivalence - (address location, value and type) check

Dual Memory management Strategy
    In Interactive mode,
        For integer,
            -5 to 256      -> no new object created
            outside bounds -> new object is created for each variable

- Python preallocates small integers in a range of -5 to 256. 
- This allocation happens during initialization and since 
   we cannot update integers (immutability) these preallocated 
   integers are singletons and are directly referenced instead 
   of reallocating. 
- This means every time we use/creates a small integer, python instead 
   of reallocating just returns the reference of preallocated one.
"""

print(f'{4 == 4   = }')
print(f'{4 == "4" = }')

print(f'{4 is 4   = }')
print(f'{4 is "4" = }')
print()

num1 = 100
num2 = 200

print(f'{num1 = }')
print(f'{num2 = }')

print(f'{num1 == num2 = }')
print(f'{num1 is num2 = }')
print(f'{id(num1) = } \t {id(num2) =}')
print()

num1 = 200

print(f'{num1 = }')
print(f'{num2 = }')
print(f'{num1 == num2 = }')
print(f'{num1 is num2 = }')
print(f'{id(num1) = } \t {id(num2) =}')
print()

num3 = 300
num4 = 300
print(f'{num3 =} \t {num4 =}')
print(f'{num3 == num4 = }')
print(f'{num3 is num4 = }')
print(f'{id(num3) = } \t {id(num4) =}')
print()


num3 = 300.33
num4 = 300.33
print(f'{num3 =} \t {num4 =}')
print(f'{num3 == num4 = }')
print(f'{num3 is num4 = }')
print(f'{id(num3) = } \t {id(num4) =}')


'''
In [1]: var1 = 256

In [2]: var2 = 256

In [3]: var1 == var2
Out[3]: True

In [4]: var1 is var2
Out[4]: True

In [5]: id(var1), id(var2)
Out[5]: (140714061084288, 140714061084288)

In [6]: 

In [6]: var3 = 258

In [7]: var4 = 258

In [8]: var3 == var4
Out[8]: True

In [9]: id(var3), id(var4)
Out[9]: (2398063480560, 2398063478256)

In [10]: var3 is var4
Out[10]: False
'''

'''
For strings, no new object is created for new variables, 
if already a variable is present with that value
In [11]: name1 = 'Udhay'

In [12]: name2 = 'Udhay'

In [13]: name1 is name2
Out[13]: True

In [14]: id(name1), id(name2)
Out[14]: (2398064123312, 2398064123312)

In [15]: name3 = 'udhaykjkjkasdkasjdkjasdhkjsahkdjhksjdksajdkdskjashkjdkjashkdjaskjdhk
    ...: jassssskkjhkjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
    ...: jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
    ...: jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
    ...: jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj'

In [16]: name4 = 'udhaykjkjkasdkasjdkjasdhkjsahkdjhksjdksajdkdskjashkjdkjashkdjaskjdhk
    ...: jassssskkjhkjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
    ...: jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
    ...: jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
    ...: jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj'

In [17]: id(name3) , id(name4)
Out[17]: (2398064362288, 2398064362288)

In [18]: name3 is name4
Out[18]: True
'''

# Assignment : Try these in interactive/Script modes for
# - None, True/False, floating-point
