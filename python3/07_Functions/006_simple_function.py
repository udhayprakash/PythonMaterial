#!/usr/bin/python
"""
Purpose: WAP to display the addition of given values
"""


# Function definition
def addition(num1, num2, num3):
    result = num1 + num2 + num3
    return result


# Function call
addition(10, 20, 30)
result = addition(10, 20, 30)
print(result)

# sum() - builtin function
# sum(10, 20, 30) # TypeError: sum expected at most 2 arguments, got 3

result = sum([10, 20, 30])
print(f'result:{result}')

result = sum([10, 20, 30], 0)
print(f'result:{result}')

result = sum([10, 20, 30], -3)
print(f'result:{result}')

result = sum((10, 20, 30, 50.))
print(f'result:{result}')

result = sum({10, 20, 30, 50.})
print(f'result:{result}')

result = sum({10: 'a', 20: 'b', 30: 'c', 50.: 'd'})
print(f'result:{result}')

result = sum({10: 'a', 20: 'b', 30: 'c', 50.: 'd'}.keys())
print(f'result:{result}')

# strings
# result = sum({10: 'a', 20: 'b', 30: 'c', 50.: 'd'}.values())
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# result = sum({'a', 'b', 'c', 'd'})
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# result = sum({'a', 'b', 'c', 'd'}, '')
# TypeError: sum() can't sum strings [use ''.join(seq) instead]

print(''.join(['a', 'b', 'c', 'd']))
print(''.join(('a', 'b', 'c', 'd')))
print(''.join({'a', 'b', 'c', 'd'}))

# -------------------------------------------
# flattening the lists
my_data = [[1, 2], [3, 4], [5, 6], [7, 8]]
# sum(my_data) # TypeError: unsupported operand type(s) for +: 'int' and 'list'
sum(my_data, [])
print(sum(my_data, []))  # [1, 2, 3, 4, 5, 6, 7, 8]

print()
my_data = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(sum(my_data, ()))

print()
my_data = [(1, 2), (3, 4), [5, 6], (7, 8)]
# print(sum(my_data,()))
# TypeError: can only concatenate tuple (not "list") to tuple

my_data = ((1, 2), 3, 4, (5, 6))
# sum(my_data)  # TypeError: unsupported operand type(s) for +: 'int' and 'tuple'

'''
Assignment
----------
1) write a function to mimick the sum() function.
Caution: don't create function with same name

2)write a function to implement the following:
    - input: ((1,2), 3,4, (5, 6))
    - output: (1, 2, 3, 4, 5, 6)
    
    HINT: isinstance() - builtin function
          int(), float(), list(), tuple(), set()
'''
print(f'isinstance(123, int)    :{isinstance(123, int)}')
print(f'isinstance(10.3, int)   :{isinstance(10.3, int)}')
print(f'isinstance(10.3, float) :{isinstance(10.3, float)}')