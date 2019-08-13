#!/usr/bin/python
"""
Purpose: closure example demo

Closures can avoid the use of global values and provides some form 
of data hiding. 
It can also provide an object oriented solution to the problem.
A closure is a way of keeping alive a variable even when the function has returned. So, in a closure, a function is defined along with the environment. In Python, this is done by nesting a function inside the encapsulating function and then returning the underlying function.
"""

def outer():
    print('In outer function')
    nnum = 786

    def inner():
        print('In Inner function', nnum)
        # default is None

    return inner #()

# outer()


# inner()  # NameError: name 'inner' is not defined
# print(nnum)  # NameError: name 'nnum' is not defined

result = outer()
print('result', type(result), result)
print('result()', result()) #inner()
# print(dir(result))

######################################################
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)

# Output: 27
print(times3(9))  # 3 * 9 = 27
print(times3(10)) # 3 * 10 = 30

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 15
print(times5(3))  # 5 * 3 = 15

# Output: 30
print(times5(times3(2)))
