# list is a mutable object
mylist = [12, 3, 4, 6]
print('mylist[2]', mylist[2])

mylist[2] = 4444
print('mylist   ', mylist)

# tuple is immutable object
mytuple = (12, 3, 4, 6)
print('mytuple[2]', mytuple[2])

# mytuple[2] = 4444  # TypeError: 'tuple' object does not support item assignment
# print(mytuple)


print((12, 4) + (99,))

other_tuple = (99,)
print(mytuple + other_tuple)
print('mytuple          ', mytuple)
print('other_tuple      ', other_tuple)

assert mytuple + other_tuple != other_tuple + mytuple
# tuple concatenation is not commutative

print('other_tuple * 3  ', other_tuple * 3)
print('3 * other_tuple  ', 3 * other_tuple)
print('other_tuple      ', other_tuple)
assert other_tuple * 3 != 3 * other_tuple
# tuple repetition is commutative
