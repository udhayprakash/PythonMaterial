from functools import reduce

# zip, map, filter, reduce
# function which were designed to work on another functions 
# are called higher-order functions 

print('\n reduce functionality')

print(reduce(lambda p, q: p + q, range(6)))
# xrange(6) - [0, 1, 2, 3, 4, 5]``
print(list(map(lambda p, q: p + q, range(6), range(6))))

mystrings = ('I', 'am', 'confident', 'about', 'myself')

print(' '.join(mystrings))

print(reduce(lambda ch1, ch2: ch1 + ' ' + ch2, mystrings))


# factorial 9 - 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
def my_factorial(given_num):
    result = 1
    for each_num in range(1, given_num + 1):
        # result = result * each_num
        result *= each_num
    return result


print(my_factorial(9))

print(reduce(lambda num1, num2: num1 * num2, range(1, 9 + 1)))

import operator

print(reduce(operator.add, [1, 3, 5, 6, 2]))
print(reduce(operator.mul, [1, 3, 5, 6, 2]))

print(reduce(operator.add, mystrings))

import itertools

# to get the intermediate values, using reduce operation
print(list(itertools.accumulate([1, 3, 5, 6, 2], lambda x, y: x + y)))
