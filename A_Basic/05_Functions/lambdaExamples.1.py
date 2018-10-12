#!/usr/bin/python

__author__ = 'udhay prakash'


def double(x):
    return x * 2


print double(12)

print 'range(6)             ', range(6)

for i in range(6):
    print double(i)

print 'map(double, range(6))', map(double, range(6))  # applying function for a list

db = lambda x: x * 2
print db(12)
print 'map(db, range(6))    ', map(db, range(6))  # applying lambda for a list

print '-' * 80

db = lambda m, n: m ** 2 + m * n - 1
print db(12, 21)


def addition(m, n):
    return m + n


print addition(23, 10)

addn = lambda p, q: p + q

print addn(23, 10)

print map(addition, range(6), range(6, 0, -1))  # applying function for a list
print map(addn, range(6), range(6, 0, -1))  # applying lambda for a list

print '-' * 80
print 'with expr'
print map(lambda x: x ** 2 - 2 * x + 12, range(5))
print map(lambda x: x * 2, range(5))
print map(lambda x: x, [(1, 2), (3, 4), (5, 6)])
print map(lambda x: x[0], [(1, 2), (3, 4), (5, 6)])
print map(lambda x: x[1], [(1, 2), (3, 4), (5, 6)])

mydict = {'a': 7, 'b': 8, 'c': 9}
print map(lambda a: a, mydict)
print map(lambda a: a, mydict.keys())
print map(lambda a: a, mydict.values())
print map(lambda a: a[1], mydict.items())

numbers = (12, 11, 12, 15, 20)
print 'numbers', numbers
numbers_sorted = sorted(numbers)
print type(numbers_sorted), numbers_sorted
print 'numbers', numbers

numbers_sorted = sorted(numbers, reverse=True)
print type(numbers_sorted), numbers_sorted

numbers = [12, 11, 12, 15, 20]
numbers.sort()
print type(numbers), numbers
numbers.sort(reverse=True)
print type(numbers), numbers

mydict = {'a': 87, 'b': 8, 'c': 19}
print map(lambda x: x, mydict.items())

print sorted(mydict.items(), key=lambda x: x[0])
print dict(sorted(mydict.items(), key=lambda x: x[1]))
print dict(sorted(mydict.items(), key=lambda x: x[1],reverse=True))

print map(lambda x: x, sorted(mydict.items(), key=lambda x: x[1]))
