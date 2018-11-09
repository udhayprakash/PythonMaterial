#!/usr/bin/python
"""
Purpose: Collections
    - Lists         []
    - Tuples        ()
    - sets          {}
    - Dictionaries  {}
"""

myEmptyList = []
print 'myEmptyList      :', myEmptyList
print 'type(myEmptyList):', type(myEmptyList)

fruits = ['Apples', 'Bananas', 'Oranges', 'Mangos']
print fruits
print type(fruits)

luckyNumbers = [3, 6, 9, 69]
print luckyNumbers
print type(luckyNumbers)

randomList = [12, 23.4, True, str(9), 876876876876, 'DevOps']
# f indexing   0    1     2     3       4               5
# reverse      -6   -5    -4    -3      -2              -1
print randomList
print type(randomList)

print '========================List Indexing============='
print 'randomList[3]:', randomList[3]
print 'randomList[0]:', randomList[0]

print 'randomList[-1]:', randomList[-1]
print 'randomList[-3]:', randomList[-3]

print '========================List Slicing============='
print 'randomList[3:5]:', randomList[3:5]
print 'randomList[3:6]:', randomList[3:6]
print 'randomList[3:58]:', randomList[3:58]
print 'randomList[6:57]:', randomList[6:57]

multiDimensionList = [1, 2, [3, 4, 5], [6, 7, 8]]
                     #0  1      2          3
                     #       0  1  2    0  1  2
print 'multiDimensionList:', multiDimensionList

print 'multiDimensionList[2]:', multiDimensionList[2]
print 'multiDimensionList[2][0]:', multiDimensionList[2][0]

print '=======================List Attributes============='
print dir(randomList)

randomList = [12, 23.4, True]

print 'randomList:', randomList
randomList.append(12)
print 'randomList:', randomList
randomList.append([99])
print 'randomList:', randomList
randomList.append(['a', 'b', 'c'])
print 'randomList:', randomList

# randomList.extend(12)  # TypeError: '
randomList.extend([12])
print 'randomList:', randomList

randomList.extend(['a', 'c'])
print 'randomList:', randomList

randomList.insert(2, 'ppp')
print 'randomList:', randomList

print 'randomList.pop():', randomList.pop()
print 'randomList:', randomList

print 'randomList.pop():', randomList.pop()
print 'randomList:', randomList

print "randomList.remove(12):", randomList.remove(12)
print 'randomList:', randomList

print 'randomList.count(12) :', randomList.count(12)
print 'randomList.count("a") :', randomList.count('a')

print 'sorted(randomList):', sorted(randomList)
print 'randomList        :', randomList

print 'randomList.sort()     :', randomList.sort()
print 'randomList        :', randomList

print randomList.reverse()
print 'randomList        :', randomList

print 'randomList[4]:', randomList[4]
print 'randomList[4][0]:', randomList[4][0]
randomList[4][0] = 1947
print 'randomList        :', randomList

print '------------------------------------------------------'
myTuple = (12, 34, 45, 56)
print myTuple, type(myTuple)

print 'myTuple[3]:', myTuple[3]
# myTuple[3] = 876876876 # TypeError: 'tuple' object does not support item assignment

print dir(myTuple)

print 'myTuple.count(34):', myTuple.count(34)
print 'myTuple.count(888):', myTuple.count(888)

print 'myTuple.index(45):', myTuple.index(45)
# print 'myTuple.index(888):', myTuple.index(888)  # ValueError:
