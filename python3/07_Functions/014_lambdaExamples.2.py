from functools import reduce

# !/usr/bin/python

__author__ = 'udhay prakash'


def printSquares(x):
    for i in range(x):
        print(i, ":", i ** 2)


printSquares(7)

print([x ** 2 for x in range(7)])

print('=' * 80)
print([x % 2 == 0 for x in range(5)])  # result is boolean
print([x for x in range(5) if x % 2 == 0])  # result is elements, which are True

print([x % 2 != 0 for x in range(5)])  # result is boolean
print([x for x in range(5) if x % 2 != 0])  # result is elements, which are True

print('+' * 80)
# zip vs map

print(list(zip('Python', 'Python')))
print(map(None, 'Python', 'Python'))

print(list(zip('Python', 'Python123')))
print(map(None, 'Python', 'Python123'))

print(list(zip(list(range(len('python'))), 'Python')))

print('=' * 80)
print(list(map(lambda a, b: a * b, [1, 2, 3, 4], [1, 2, 3, 4])))
print(reduce(lambda a, b: a * b, [1, 2, 3, 4]))  # results in 1*2*3*4

print(reduce((lambda a, b: a ** b), [1, 2, 3, 4]))  # results in 1**2**3**4; anything to the power of 1 results in 1
print(reduce((lambda a, b: a ** b), [2, 3, 4]))  # results in 2**3**4

string1 = 'I am confident about my Success'
list_of_content = string1.split(' ')
print(list_of_content)

print(' '.join(list_of_content))
print(reduce(lambda a, b: a + ' ' + b, list_of_content))
