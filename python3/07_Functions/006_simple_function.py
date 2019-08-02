
# function definition
def add(a,b, c):  # arguments - a,b,c
    sum1 = a + b + c
    return sum1

# function call 
print(add(12, 34, 56))  # parameters - 1,2,3

# Built-in function 
# sum()

# print( sum(12, 34, 56) )

print(sum((12, 34, 56)))
print(sum([12, 34, 56]))
print(sum({12, 34, 56}))

print(sum([[1, 2], [3, 4], [5, 6, 7]], []))
print(sum(([1, 2], [3, 4], [5, 6, 7]), []))
# print(sum(((1, 2), [3, 4], [5, 6, 7]), []))
# print(sum(((1, 2), (3, 4), (5, 6, 7)), []))
print(sum(((1, 2), (3, 4), (5, 6, 7)), ()))

# print(sum((1, 2, 3, 4, (5, 6, 7)), ()))
# Assignment 
