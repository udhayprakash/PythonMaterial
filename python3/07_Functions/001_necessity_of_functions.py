#!/usr/bin/python3
"""
Purpose: Functions
            - code re-usability
            - To modularize the problem
            - Better maintenance of the code

    Functions are called as first class objects in python

    Function with no arguments and no return value
"""
# Method1
print("Hello world")
print("Hello world")
print("Hello world")
print("Hello world")
print()


def hello():
    print("Hello world")


hello()
hello()
hello()
hello()
print()

# ============================================
# Method 1
n = 9
binomial_expr = n**2 + 3 * n + 3
print(binomial_expr)

n = 34
binomial_expr = n**2 + 3 * n + 3
print(binomial_expr)

n = -0.98798
binomial_expr = n**2 + 3 * n + 3
print(binomial_expr)
print()


# Method 2
def binomial_expression(x):
    binomial_expr = x**2 + 3 * x + 3
    print(binomial_expr)


binomial_expression(9)
binomial_expression(34)
binomial_expression(-0.98798)
print()

# ============================================
lower_bound = 0
upper_bound = 10

even_nums = []
for i in range(lower_bound, upper_bound):
    if i % 2 == 0:
        even_nums.append(i)
print(even_nums)

lower_bound = 45
upper_bound = 67

even_nums = []
for i in range(lower_bound, upper_bound):
    if i % 2 == 0:
        even_nums.append(i)
print(even_nums)


# Method 2 - using functions
def get_even_nums(min_val, max_val):
    even_nums = []
    for i in range(min_val, max_val):
        if i % 2 == 0:
            even_nums.append(i)
    print(even_nums)


print()
get_even_nums(0, 10)
get_even_nums(45, 67)
get_even_nums(-3, 5)
get_even_nums(-34, 5)
get_even_nums(-3, 85)
