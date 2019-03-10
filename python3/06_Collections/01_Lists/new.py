
mylist = [1, 2, 3]
#         0  1  2
print('running_ports', mylist)
print('type(running_ports)', type(mylist))

print('running_ports[2]', mylist[2])
mylist[2] = '3333'
print('running_ports[2]', mylist[2])

print('running_ports', mylist)

print('-------------tuple')

mytuple = (1, 2, 3)
print('mytuple', mytuple)
print('type(mytuple)', type(mytuple))

print('mytuple[2]', mytuple[2])
# mytuple[2] = '33333'
# TypeError: 'tuple' object does not support item assignment


myTuple = (12, 34, 45, 56)
print(myTuple, type(myTuple))

print('myTuple[3]:', myTuple[3])
# myTuple[3] = 876876876 # TypeError: 'tuple' object does not support item assignment

print(dir(myTuple))

print('myTuple.count(34):', myTuple.count(34))
print('myTuple.count(888):', myTuple.count(888))

print('myTuple.index(45):', myTuple.index(45))
# print 'myTuple.index(888):', myTuple.index(888)  # ValueError:
