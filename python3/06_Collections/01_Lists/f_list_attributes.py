#!/usr/bin/python3
"""
Purpose: List Attributes
    index,reverse,sort,
    sorted(), reversed()
"""
# list.index - gives the position of an element in that list
numbers = [123, 324, 2, 213, 125, 125]
#           0   1    2   3    4    5
print(f"{numbers            =}")
print(f"{numbers[4]         =}")  # 125
# print(f'{numbers.index(4) =}')  # ValueError: 4 is not in list
print(f"{numbers.index(125) =}")  # 4 - first occurrence
print(f"{numbers.index(324) =}\n")  # 1

# Question: list.sort() vs sorted()
print(f"{numbers            =}")
print(f"{sorted(numbers)    =}")
print("After sorted(numbers)=", numbers)
print()

# sorting will be done in ascending order
# sorted() will not change original object
print(f"{numbers            =}")
print(f"{numbers.sort()     =}")
print("After numbers.sort()=", numbers)
# List.sort() will change the original object


print(f"{sorted(numbers, reverse=True) =}")
print()
print(f"{numbers =}")
numbers.sort(reverse=True)
print("After numbers.sort(reverse =True)\n\t", numbers)
print()

mylist = [1, 2, 9, "1", "2", "9", "a", "z", "A", "Z", True, False, None]
# print(f'{sorted(mylist) =}')
# TypeError: '<' not supported between instances of 'str' and 'int'


mylist = ["1", "2", "9", "a", "z", "A", "Z", True, False, None]
# print(f'{sorted(mylist) =}')
# TypeError: '<' not supported between instances of 'bool' and 'str'

mylist = [1, 2, 9, True, False, None]
# print(f'{sorted(mylist) =}')
# TypeError: '<' not supported between instances of 'NoneType' and 'bool'

mylist = [1, 2, 9, True, False]
print(f"{sorted(mylist) =}")  # [False, 1, True, 2, 9]

sorted([False, 0])
sorted([1, 1.0])

# Question: list.sort(reverse=True), sorted(mylist, reverse=True) vs reversed()
mylist = ["1", "2", "9", "a", "z", "A", "Z"]
# NOTE: sorting based on ascii position
print(f"{sorted(mylist)              =}")  # ['1', '2', '9', 'A', 'Z', 'a', 'z']
print(f"{sorted(mylist, reverse=True)=}")  # ['z', 'a', 'Z', 'A', '9', '2', '1']

print(
    f"{reversed(mylist)            =}"
)  # <list_reverseiterator object at 0x0000023D0BC97D90>

# NOTE: Just reversing the sequence, in terms of definition order
print(f"{list(reversed(mylist)) =}")  # ['Z', 'A', 'z', 'a', '9', '2', '1']


mylist = ["1", 1, True, None, 123.32]
print(
    f"{list(reversed(mylist)) =}"
)  # [123.32, None, True, 1, '1'] - PREFERRED FOR LARGE SEQUENCES
print(
    f"{mylist[::-1]           =}"
)  # [123.32, None, True, 1, '1'] - PREFERRED FOR SMALL LENGTHS
