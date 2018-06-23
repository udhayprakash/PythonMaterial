
mylist = [1, 2, 3]
#         0  1  2
print 'mylist', mylist
print 'type(mylist)', type(mylist)

print 'mylist[2]', mylist[2]
mylist[2] = '3333'
print 'mylist[2]', mylist[2]

print 'mylist', mylist

print '-------------tuple'

mytuple = (1, 2, 3)
print 'mytuple', mytuple
print 'type(mytuple)', type(mytuple)

print 'mytuple[2]', mytuple[2]
# mytuple[2] = '33333'
# TypeError: 'tuple' object does not support item assignment
