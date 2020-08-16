#!/usr/bin/python
"""
Purpose: closures in python
Purpose: closures in python
    - Closures can avoid the use of global values.
    - It provides some form of data hiding.
    - When there are few methods (one method in most cases) to be implemented in a 
      class, closures can provide a better solution. But when the number of attributes
      and methods are more, it is better to implement a class.
    - It is a way of keeping alive a variable even when the function has returned. 
      So, in a closure, a function is defined along with the environment. 
      In Python, this is done by nesting a function inside the encapsulating function 
      and then returning the underlying function.

"""

# function definition


def outer():
    print('outer function - start ')

    def inner():
        print('inner function - start')
        return 'something'

    # case 1:
    # return inner()

    # case 2:
    return inner


# function call
if __name__ == '__main__':
    result = outer()
    print(f'{type(result)} {result}')
    # inner() NameError: name 'inner' is not defined
    result()

    outer()()


# --------------------------------------------------
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


# Multiplier of 3
mul3 = make_multiplier_of(3)
print(f'{type(mul3)} {mul3}')

print(f'mul3(10):{mul3(10)}')
print(f'mul3(7) :{mul3(7)}')

mul5 = make_multiplier_of(5)
print(f'{type(mul5)} {mul5}')

print(f'mul5(10):{mul5(10)}')
print(f'mul5(7) :{mul5(7)}')
