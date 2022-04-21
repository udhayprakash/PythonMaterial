#!/usr/bin/python

__author__ = 'udhay prakash'


def double(x):
    return x * 2

# functions are treated as first class object

print(double(12))

print('range(6)             ', list(range(6)))

new_list = []
for i in range(6):
    new_list.append(double(i))
print(new_list)

# map(function, iterable1, iterable2, ..)
# iterable objects - str, list, tuple, set, dictionary
print('map(double, range(6))', list(map(double, list(range(6)))))  # applying function for a list

db = lambda x: x * 2
print(db(12))
print('map(db, range(6))    ', list(map(db, list(range(6)))))  # applying lambda for a list
print('map(lambda x: x * 2, range(6))', [x * 2 for x in range(6)])  # applying lambda for a list

print('-' * 50)

def sme_operation(m, n):
    return m ** 2 + m * n - 1

print(sme_operation(12, 21))

db = lambda m, n: m ** 2 + m * n - 1
print(db(12, 21))

print('-' * 50)

def addition(m, n):
    return m + n

print(addition(23, 10))

addn = lambda p, q: p + q

print(addn(23, 10))

print(list(map(addition, list(range(6)), list(range(6, 0, -1)))))  # applying function for a list
print(list(map(addn, list(range(6)), list(range(6, 0, -1)))))  # applying lambda for a list

print('-' * 80)
print('with expr')
print([x ** 2 - 2 * x + 12 for x in range(5)])
print([x * 2 for x in range(5)])
print([x for x in [(1, 2), (3, 4), (5, 6)]])
print([x[0] for x in [(1, 2), (3, 4), (5, 6)]])
print([x[1] for x in [(1, 2), (3, 4), (5, 6)]])
print()

mydict = {'a': 7, 'b': 8, 'c': 9}
print([a for a in mydict])
print([a for a in list(mydict.keys())])
print([a for a in list(mydict.values())])
print([a[1] for a in list(mydict.items())])

numbers = (12, 11, 12, 15, 20)
print('numbers', numbers)
numbers_sorted = sorted(numbers)
print(type(numbers_sorted), numbers_sorted)
print('numbers', numbers)

numbers_sorted = sorted(numbers, reverse=True)
print(type(numbers_sorted), numbers_sorted)

numbers = [12, 11, 12, 15, 20]
numbers.sort()
print(type(numbers), numbers)
numbers.sort(reverse=True)
print(type(numbers), numbers)

mydict = {'a': 87, 'b': 8, 'c': 19}
print([x for x in list(mydict.items())])

print(sorted(list(mydict.items()), key=lambda x: x[0]))
print(dict(sorted(list(mydict.items()), key=lambda x: x[1])))
print(dict(sorted(list(mydict.items()), key=lambda x: x[1],reverse=True)))

print([x for x in sorted(list(mydict.items()), key=lambda x: x[1])])
