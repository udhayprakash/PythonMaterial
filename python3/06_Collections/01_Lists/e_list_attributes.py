#!/usr/bin/python3
"""
Purpose: List Attributes
"""
mylist = [11, 22, 33]
for each_attribute in dir(mylist):
    if not each_attribute.startswith("__"):
        print(each_attribute, end=",")
print()  # append,clear,copy,extend,index,insert,pop,remove,reverse,sort

print(f"{mylist                 =}")  # [11, 22, 33]

# Question: append vs Extend vs insert
mylist.append(44)
print("After mylist.append(44)  :", mylist)  # [11, 22, 33, 44]

mylist.append(None)
print("After mylist.append(None):", mylist)  # [11, 22, 33, 44, None]

mylist.append([55, 66])
print("After mylist.append([55, 66]):\n\t", mylist)  # [11, 22, 33, 44, None, [55, 66]]
print()

# mylist.extend(77)
# TypeError: 'int' object is not iterable

# iterables - string, collections(list, tuple, set, dict), range, iterator, generator

mylist.extend([77])
print("After mylist.extend([77]):\n\t", mylist)

mylist.extend((88, 99))
print("After mylist.extend((88, 99)):\n\t", mylist)

mylist.extend([111, (222, 333)])
print("After mylist.extend([111, (222, 333)])\n\t", mylist)
print()

# NOTE: Both list.append and list.extend CAN add at the end of list only
# 1. list.append - can take single element, or an iterable. Adds as it is
# 2. list.extend will take only iterable. Adds to same dimension

mylist = [11, 22, 33]
print(f"{mylist                 =}")  # [11, 22, 33]

mylist.insert(0, "a")
print("After mylist.insert(0, 'a'):\n\t", mylist)

mylist.insert(3, "b")
print("After mylist.insert(3, 'b'):\n\t", mylist)

mylist.insert(3, ["c", "d"])
print("After mylist.insert(3, ['c', 'd']):\n\t", mylist)

# Question: How to make list.insert to work like list.append
mylist.insert(-1, "eeeeee")
print("After mylist.insert(-1, 'eeeeee'):\n\t", mylist)

mylist.insert(len(mylist), "ff")
print("After mylist.insert(len(mylist), 'ff'):\n\t", mylist)
print()

# Question: list.insert vs substitution
print(f"{mylist[3] =}")
mylist[3] = "god"
print("After mylist[3] = 'god':\n\t", mylist)

# mylist[33] = 'god'
# IndexError: list assignment index out of range
mylist.insert(33, "mad")
print("After mylist.insert(33, 'mad'):\n\t", mylist)
print()

# Question: list.pop() vs list.remove()
print(f"{mylist.pop() =}")
print(f"{mylist       =}\n")

print(f"{mylist.pop() =}")
print(f"{mylist       =}\n")

mylist = ["a", 11, 22, "god", "b", (12, [323, 3])]
print(f"{mylist.pop() =}")
print(f"{mylist       =}\n")

# To remove a specific element
print(f"{mylist.remove(11) =}")  # None
print(f"{mylist       =}\n")  # ['a', 22,  'god', 'b']

# If multiple elements are present, it will remove the first occurrence
mylist = [[22], 11, 22, 33, 22, 22, 33]
print(f"{mylist.remove(22) =}")
print(f"{mylist       =}\n")

# mylist.remove('q')
# ValueError: list.remove(x): x not in list

# mylist = []
# mylist.pop()
# IndexError: pop from empty list


# del - can remove an element or some indexed positions
mylist = ["a", "b", "c", "d", "e", "f"]
print(f"{mylist       =}")
print(f"{mylist[3]    =}")
del mylist[3]
print("After del mylist[3]   =", mylist)


print(f"{mylist[0::2]          =}")
del mylist[0::2]
print("After del mylist[0::2]:", mylist)


# Question: list.clear vs del list
mylist.clear()
print("After mylist.clear()  :", mylist)

del mylist
# print(mylist)
# NameError: name 'mylist' is not defined
