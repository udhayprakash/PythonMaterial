#!/usr/bin/python
"""
Purpose: closure example demo

Closures can avoid the use of global values and provides some form 
of data hiding. 
It can also provide an object oriented solution to the problem.
A closure is a way of keeping alive a variable even when the function has returned. So, in a closure, a function is defined along with the environment. In Python, this is done by nesting a function inside the encapsulating function and then returning the underlying function.
"""
from math import pi

pi = 300
mydict = {'lang': 'python'}


# function definition
def outer():
    print('outer function - start ')
    pi = 200
    mydict = {'lang': 'ruby'}

    def inner():
        pi = 100
        mydict = {'lang': 'golang'}
        print('inner function - start')
        print(f'pi              :{pi}')
        print(f'mydict["lang"]  :{mydict["lang"]}')
        return 'something'

    # case 1:
    # return inner()

    # case 2:
    return inner


# function call
if __name__ == '__main__':
    result = outer()
    print(f'{type(result)} {result}')
    print('\n\ncalling inner() via result()')
    result()



# # --------------------------------------------------
# def make_multiplier_of(n):
#     def multiplier(x):
#         return x * n
#     return multiplier
#
# # Multiplier of 3
# mul3 = make_multiplier_of(3)
# print(f'{type(mul3)} {mul3}')
#
# print(f'mul3(10):{mul3(10)}')
# print(f'mul3(7) :{mul3(7)}')
#
# mul5 = make_multiplier_of(5)
# print(f'{type(mul5)} {mul5}')
#
# print(f'mul5(10):{mul5(10)}')
# print(f'mul5(7) :{mul5(7)}')
#
