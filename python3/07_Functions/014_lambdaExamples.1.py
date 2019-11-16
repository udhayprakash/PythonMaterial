#!/usr/bin/python
"""
Purpose: Lambda (or) Anonymous functions
"""
__author__ = 'udhay prakash'


def double(x):
    return x * 2


print(f'double(2):{double(2)}')
print(f'double(3):{double(3)}')

dbl = lambda x: x * 2
print(f'dbl(2)   :{dbl(2)}')
print(f'dbl(3)   :{dbl(3)}')

assert double(2) == dbl(2)


# ------------------------------------
def binomial_expression(n):
    return n ** 2 + 2 * n - 6


print(f'binomial_expression(10) :{binomial_expression(10)}')

binexp = lambda n: n ** 2 + 2 * n - 6
print(f'binexp(10)              :{binexp(10)}')
print()


# -----------------------------------------------
def hello(first_name, last_name):
    return f'Hello {first_name} {last_name} !!!'


h = lambda fn, ln: f'Hello {fn} {ln} !!!'

assert hello('Gudo', 'Russum') == h('Gudo', 'Russum')


# ---------------------------------------------------
def test_evenness(num):
    # if num % 2 == 0:
    #     return 'even'
    # else:
    #     return 'odd'

    return 'even' if num % 2 == 0 else 'odd'


tevl = lambda num: 'even' if num % 2 == 0 else 'odd'

assert test_evenness(222) == tevl(222)
assert test_evenness(123) == tevl(123)
assert test_evenness(123) == (lambda num: 'even' if num % 2 == 0 else 'odd')(123)

# --------------------------------------------------------
my_tuple = (12, 34, 45, 56, 67, 78, 90)


#           0    1  2   3   4  5    6

def get_index_of(given_tuple, search_value):
    return given_tuple.index(search_value)


get_index_l = lambda gvn_t, sv: gvn_t.index(sv)

assert get_index_of(my_tuple, 56) == get_index_l(my_tuple, 56)

###############################################
# Method 1
odd_nums = []
for num in range(9):
    if num % 2:
        odd_nums.append(num)

print(odd_nums)

# Method 2: list comprehension
odd_nums1 = [num for num in range(9) if num % 2]
print(odd_nums1)


# Method 3: applying functions
def is_odd(n):
    return True if n % 2 else False


odd_nums2 = []
for num in range(9):
    if is_odd(num):
        odd_nums2.append(num)

print(odd_nums2)

# Method 4: applying functions
odd_nums3 = list(map(is_odd, range(9)))
print(odd_nums3)

odd_nums3 = list(filter(is_odd, range(9)))
print(odd_nums3)

# Method 4: applying lambdas
odd_nums3 = list(map(lambda x: x % 2, range(9)))
print(odd_nums3)

odd_nums3 = list(filter(lambda x: x % 2, range(9)))
print(odd_nums3)

'''
Assignment: 
----------
1) Try to get the prime numbers between 1208 and 4893
'''