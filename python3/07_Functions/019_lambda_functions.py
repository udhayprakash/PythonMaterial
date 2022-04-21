#!/usr/bin/python3
"""
Purpose: Lambda (or) Anonymous functions
"""
import sys


def double(x):
    return x * 2


print(f'double(2):{double(2)}')
print(f'double(3):{double(3)}')

dbl = lambda x: x * 2
print(f'dbl(2)   :{dbl(2)}')
print(f'dbl(3)   :{dbl(3)}')

assert double(2) == dbl(2)
assert double(3) == dbl(3)

assert double(3) == (lambda x: x * 2)(3)

print(type(double), type(dbl))
print(f'sys.getsizeof(double):{sys.getsizeof(double)}')
print(f'sys.getsizeof(dbl)   :{sys.getsizeof(dbl)}')
print()


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
def check_evenness(num):
    # if num % 2 == 0:
    #     return 'even'
    # else:
    #     return 'odd'
    return 'even' if num % 2 == 0 else 'odd'


tevl = lambda num: 'even' if num % 2 == 0 else 'odd'
assert check_evenness(222) == tevl(222)
assert check_evenness(123) == tevl(123)
assert check_evenness(123) == (lambda num: 'even' if num % 2 == 0 else 'odd')(123)

# --------------------------------------------------------
my_tuple = (12, 34, 45, 56, 67, 78, 90)


#           0    1  2   3   4    5   6

def get_index_of(given_tuple, search_value):
    return given_tuple.index(search_value)


get_index_l = lambda gvn_t, sv: gvn_t.index(sv)

assert get_index_of(my_tuple, 56) == get_index_l(my_tuple, 56)


# ---------------------------------------------------------------
def wish(message):
    # return message
    return lambda name: message.upper() + ' ' + name


greet = wish('Happy Birthday')
print(greet)
print(greet('Sushmitha'))

# ----- Lambda with no args
myfunc = lambda: 'hello! no args given'
print(f'{myfunc() = }')
print(f'{myfunc() = }')
print()

# ----- Lambda with args not used
myfunc = lambda name: 'hello! My name is name'
print(f'{myfunc("Udhay") = }')
print(f'{myfunc("Neha") = }')
print()

# ----- Lambda with args used
myfunc = lambda name: f'hello! My name is {name}'
print(f'{myfunc("Udhay") = }')
print(f'{myfunc("Neha") = }')
