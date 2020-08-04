#!/usr/bin/python3
"""
Purpose: List Attributes
    index,reverse,sort,
    sorted(), reversed()
"""
# list.index - gives the postion of an element in that list
numbers = [123, 324, 2, 213, 125, 125]
#           0   1    2   3    4    5
print(f'{numbers            =}')
print(f'{numbers.index(2)   =}')  # 2
# print(f'{numbers.index(3)   =}')
# ValueError: 3 is not in list
print(f'{numbers.index(324) =}\n')  # 1

# Question: list.sort() vs sorted() 
print(f'{numbers            =}')
print(f'{sorted(numbers)    =}')
print('After sorted(numbers)=', numbers)
print()

# sorting will be done in ascending order
# sorted() will not change orginal object
print(f'{numbers            =}')
print(f'{numbers.sort()     =}')
print('After numbers.sort()=', numbers)
# List.sort() will change the orginal object

print(f'{sorted(numbers, reverse=True) =}')
print()
print(f'{numbers =}')
numbers.sort(reverse =True)
print("After numbers.sort(reverse =True)\n\t", numbers)
print()

mylist = [1, 2, 9, '1', '2', '9', 'a', 'z', 'A', 'Z', True, False, None]
# print(f'{sorted(mylist) =}')
# TypeError: '<' not supported between instances of 'str' and 'int'

mylist = ['1', '2', '9', 'a', 'z', 'A', 'Z', True, False, None]
# print(f'{sorted(mylist) =}')
# TypeError: '<' not supported between instances of 'bool' and 'str'


# Question: list.sort(reverse=True), sorted(mylist, reverse=True) vs reversed()
mylist = ['1', '2', '9', 'a', 'z', 'A', 'Z']
# NOTE: sorting based on ascii position
print(f'{sorted(mylist)              =}')  # ['1', '2', '9', 'A', 'Z', 'a', 'z']
print(f'{sorted(mylist, reverse=True)=}')  # ['z', 'a', 'Z', 'A', '9', '2', '1']

print(f'{reversed(mylist)            =}')  # <list_reverseiterator object at 0x0000023D0BC97D90>

# NOTE: Just reversing the sequence, in terms of definition order
print(f'{list(reversed(mylist)) =}')  # ['Z', 'A', 'z', 'a', '9', '2', '1']

