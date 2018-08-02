# list is a mutable object
mylist = [12, 3, 4, 6]
print mylist[2]

mylist[2] = 4444
print mylist


# tuple is immutable object
mytuple = (12, 3, 4, 6)
print mytuple[2]

mytuple[2] = 4444  # TypeError: 'tuple' object does not support item assignment
print mytuple
