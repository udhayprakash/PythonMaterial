#!/usr/bin/python
"""
Purpose:

Lambda functions or 
Anonymous functions
"""
__author__ = 'udhay prakash'


def double(x):
    return x * 2

print(double(12))  # 24

dbl = lambda x: x*2
print(dbl(12))
print((lambda x:x*2)(12))
#############################################

# def binomial_expression(n):
#     return n**2 - 2*n + 1

# print(binomial_expression(9))
# print((lambda n: n**2 - 2*n + 1)(9))
# ##############################################

# def test_evenness(num):
#     # if num % 2 == 0:
#     #     return 'even'
#     # else:
#     #     return 'odd'
#     return 'even' if num % 2 == 0 else 'odd'
    
# print(test_evenness(45))
# print((lambda num: 'even' if num % 2 == 0 else 'odd')(45))


# def get_values(given_tuple, given_position):
#     return given_tuple[given_position]

# my_tuple = (12, 34, 45, 56, 67 ,78, 90)
#         #    0    1  2   3   4  5    6
# print(get_values(my_tuple, 4))

# print((lambda tp, ps: tp[ps])(my_tuple, 4))

########################################
print( list(range(6)))

new_list = []
for i in range(6):
    new_list.append(double(i))
print(new_list)

new_list = []
for i in range(6):
    new_list.append((lambda x:x*2)(i))
print(new_list)

# map(function, iterable1, iterable2, ..)
# iterable objects - str, list, tuple, set, dictionary
print('map(double, range(6))       :', list(map(double, range(6))))  # applying function for a list
print('map(lambda x: x*2, range(6)):', list(map(lambda x: x*2, range(6))))  # applying function for a list

print('-' * 50)
#######################################
def addition(m, n):
    return m + n

print(addition(23, 10))

print((lambda p, q: p + q)(23, 10))

# [1, 2, 3] + [3, 4, 5] => [1, 2, 3, 3, 4, 5]
# [1, 2, 3] , [3, 4, 5] => [4 , 6, 8]

print(list(map(addition,           [1, 2, 3], [3, 4, 5])))
print(list(map(lambda p, q: p + q, [1, 2, 3], [3, 4, 5])))


# [1, 2, 3] , [3, 4, 5] => [(1, 3), (2, 4), (3, 5)]
print(list(zip([1, 2, 3] , [3, 4, 5])))
print(list(map(lambda x,y:(x,y), [1, 2, 3], [3, 4, 5])))

print('-' * 80)
print('with expr')
print([x ** 2 - 2 * x + 12 for x in range(5)])
print([x * 2 for x in range(5)])
print([x for x in [(1, 2), (3, 4), (5, 6)]])
print([x[0] for x in [(1, 2), (3, 4), (5, 6)]])
print([x[1] for x in [(1, 2), (3, 4), (5, 6)]])
print()

# # mydict = {'a': 7, 'b': 8, 'c': 9}
# # print([a for a in mydict])
# # print([a for a in list(mydict.keys())])
# # print([a for a in list(mydict.values())])
# # print([a[1] for a in list(mydict.items())])

# numbers = (12, 11, 12, 15, 20)
# print('numbers', numbers)
# numbers_sorted = sorted(numbers)
# print(type(numbers_sorted), numbers_sorted)
# print('numbers', numbers)

# numbers_sorted1 = sorted(numbers_sorted, reverse=True)
# print(numbers_sorted, numbers_sorted1)

# numbers = [12, 11, 12, 15, 20]
# numbers.sort()
# print(type(numbers), numbers)
# numbers.sort(reverse=True)
# print(type(numbers), numbers)

