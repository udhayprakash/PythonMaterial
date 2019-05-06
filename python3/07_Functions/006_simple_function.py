
# function definition
def add(a,b, c):  # arguments - a,b,c
    sum1 = a + b + c
    return sum1

# function call 
print(add(12, 34, 56))  # parameters - 1,2,3
print(add(12, 34, 56))  # parameters - 1,2,3

ans =  add(12, 34, 56)  # parameters - 1,2,3
print('ans * 2', ans * 2)

# print(sum1) # NameError: name 'sum1' is not defined


# Built-in function 
# sum()

# print(sum(12, 34, 56))
print(sum((12, 34, 56)))
# print(sum(1)) # TypeError: 'int' object is not iterable