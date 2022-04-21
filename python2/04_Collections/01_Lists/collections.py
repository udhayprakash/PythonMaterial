#!/usr/bin/python
"""
Purpose: Collections
    - Lists         []
    - Tuples        ()
    - sets          {}
    - Dictionaries  {}
"""

myEmptyList = [] # list()
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

print 'randomList.remove(12):', randomList.remove(12)
print 'randomList:', randomList

print 'randomList.count(12) :', randomList.count(12)
print 'randomList.count("a") :', randomList.count('a')
print "randomList.count(['a', 'b', 'c'])", randomList.count(['a', 'b', 'c'])

# sorted() and list.sort() - TIM sort algorithm
print
print 'sorted(randomList):', sorted(randomList)
print 'randomList        :', randomList

print 'randomList.sort()     :', randomList.sort()
print 'randomList        :', randomList

print
print 'sorted(randomList, reverse=True):', sorted(randomList, reverse=True)
print 'reversed(randomList)', reversed(randomList)
print 'randomList        :', randomList


print 'randomList.reverse()', randomList.reverse()
print 'randomList        :', randomList

print 'randomList[4]:', randomList[4]
print 'randomList[4][0]:', randomList[4][0]
randomList[4][0] = 1947
print 'randomList        :', randomList

print '------------------------------------------------------'
