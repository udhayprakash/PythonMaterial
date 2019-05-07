#!/usr/bin/python
"""
Purpose: closure example demo

Closures can avoid the use of global values and provides some form 
of data hiding. 
It can also provide an object oriented solution to the problem.
"""

def outer():
    print('In outer function')
    nnum = 786

    def inner():
        print('In Inner function', nnum)
        # default is None

    return inner#() # function


result = outer()
print('result', type(result), result)
print('result()', result())
print(dir(result))
# inner()  # NameError: name 'inner' is not defined

# print nnum  # NameError: name 'nnum' is not defined

# def make_multiplier_of(n):
#     def multiplier(x):
#         return x * n
#     return multiplier

# # Multiplier of 3
# times3 = make_multiplier_of(3)

# # Multiplier of 5
# times5 = make_multiplier_of(5)

# # Output: 27
# print(times3(9))

# # Output: 15
# print(times5(3))

# # Output: 30
# print(times5(times3(2)))
