#!/usr/bin/python
# -*- coding: utf-8 -*-

mylist = [12, 34.8, 500000, [6, 8], (5,)]
print('type(mylist)', type(mylist))
print('len(mylist)', len(mylist))

mytuple = (12, 34.8, 500000, [6, 8], (5,))
print('type(mytuple)', type(mytuple))
print('len(mytuple)', len(mytuple))
print(mytuple)

print()
another_tuple = (99.9,)
print('type(another_tuple)', type(another_tuple))
print('len(another_tuple)', len(another_tuple))

print()
empty_tuple = tuple()  # ()
print('type(empty_tuple)', type(empty_tuple))
print('len(empty_tuple)', len(empty_tuple))

mytuple = 1, 2, 3
print('type(mytuple)', type(mytuple))
print('len(mytuple)', len(mytuple))
print(mytuple)

print()
print('dir(empty_tuple)\n', dir(empty_tuple))
for each in dir(empty_tuple):
    if not each.startswith('__'):
        print(each)

# # mytuple = (12, 34, 5, 6, 8, (5,))
# # print('mytuple', mytuple)
# # print('mytuple.count(5):', mytuple.count(5))

# # mytuple = (12, 34, 5, 6, 8, (5))
# # print('mytuple', mytuple)
# # print('mytuple.count(5):', mytuple.count(5))

# # print('mytuple.index(34):', mytuple.index(34))
# # print('mytuple.index(5) :', mytuple.index(5))
# # # print('mytuple.index(999) :', mytuple.index(999)) ValueError: tuple.index(x): x not in tuple

# # # strictly type language
# # result = (9,99) + (9,) # tuple concatenation
# # print('result', result)

# # result = (9,99) + tuple([22, 44 , 454, 565, 5]) # tuple concatenation
# # print('result', result)

# # print(list('python programming'))
# # print(tuple('python programming'))
# # print()
# # # tuples are immutable 
# # print('mytuple', mytuple, id(mytuple))
# # # mytuple[2] = '2.2222' # TypeError: 'tuple' object does not support item assignment

# # print('overwriting')
# # mytuple = (12, 34, '2.2222', 6, 8, (5,))
# # print('mytuple', mytuple, id(mytuple))
