#!/usr/bin/python3
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
print(f"result:{result}")

# --- sum() - builtin function for adding values
# sum(10, 20, 30) # TypeError: sum() takes at most 2 arguments (3 given)

# help(sum) :-> sum(iterable, /, start=0)
result = sum([10, 20, 30])
print(f"result:{result}")

result = sum({10, 20, 30})
print(f"result:{result}")

result = sum((10, 20, 30))
print(f"result:{result}")

result = sum((10, 20, 30), 0)
print(f"result:{result}")  # 60

result = sum((10, 20, 30), -10)
print(f"result:{result}")  # 50

result = sum((10, 20, 30), 3)
print(f"result:{result}")  # 63

result = sum((10, 20, 30, 50.0))
print(f"result:{result}")

result = sum({10, 20, 20, 30, 50.0})
print(f"result:{result}")

result = sum({10: "a", 20: "b", 30: "c", 50.0: "d"})
print(f"result:{result}")  # by default, dict gives keys when iterating

result = sum({10: "a", 20: "b", 30: "c", 50.0: "d"}.keys())
print(f"result:{result}")

# strings

# result = sum({10: 'a', 20: 'b', 30: 'c', 50.: 'd'}.values())
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# result = sum({10: 'a', 20: 'b', 30: 'c', 50.: 'd'}.values(), '')
# TypeError: sum() can't sum strings [use ''.join(seq) instead]

print("".join(["a", "b", "c", "d"]))
print("".join(("a", "b", "c", "d")))
print("".join({"a", "b", "c", "d"}))

# -------------------------------------------
# Question: flattening the lists
my_data = [[1, 2], [3, 4], [5, 6], [7, 8]]

# Method 1:
flat_data = []
for each in my_data:
    # print(each, type(each))
    # flat_data.append(each)
    # flat_data.extend(each)
    flat_data += each

print(f"{flat_data =}")

# Method 2:
# sum(my_data) # TypeError: unsupported operand type(s) for +: 'int' and 'list'
# sum(my_data, 0) # TypeError: unsupported operand type(s) for +: 'int' and 'list'

print(sum(my_data, []))

print()
my_data = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(sum(my_data, ()))

print()
# my_data = [{1, 2}, {3, 4}, {5, 6}, {7, 8}]
# print(sum(my_data, set()))
# TypeError: unsupported operand type(s) for +: 'set' and 'set'


# my_data = ((1, 2), [3, 4], (5, 6))
# sum(my_data, ()) # TypeError: can only concatenate tuple (not "list") to tuple


# my_data = ((1, 2), 3, 4, (5, 6))
# sum(my_data, ()) # TypeError: can only concatenate tuple (not "int") to tuple


"""
Assignment
----------
1) write a function to mimick the sum() function.
    Caution: don't create function with same name

2) write a function to implement the following:
    - input: ((1,2), 3,4, [5, 6])
    - output: (1, 2, 3, 4, 5, 6)

    HINT: isinstance() - builtin function
          int(), float(), list(), tuple(), set()
          list.append(), list.extend
          list & tuple concatenation
"""
# print(f'type(int) is type(123)  :{type(int) is type(123)}')
print(f"isinstance(123, int)    :{isinstance(123, int)}")

print(f"isinstance(10.3, int)   :{isinstance(10.3, int)}")
print(f"isinstance(10.3, float) :{isinstance(10.3, float)}")
