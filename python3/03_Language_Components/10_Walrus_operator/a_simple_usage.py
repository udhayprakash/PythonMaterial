"""
Purpose: Assignment Expression (OR) Walrus Operator

Introducted in python 3.8

PEP 572 describes all the details of assignment expressions

In simple words, It will combine assignment + some expression
"""

# Example Usage Case 1
value1 = 100
print("value1 = ", value1)

print("value2 = ", value2 := 200)


# Example Usage Case 2
num1 = 123
if num1 % 2:
    print("Num is ODD")

if (num1 := 123) % 2:
    print("Num is ODD")

# Example Usage Case 3
num1 = int(input("num1 = "))
if num1 % 2:
    print("Num is ODD")

if (num1 := int(input("num1 = "))) % 2:
    print("Num is ODD")

# Example Usage Case 4
a = [1, 2, 3, 4]
n = len(a)
if n > 3:
    print(f"List is too long ({n} elements, expected <= 3)")

a = [1, 2, 3, 4]
if (n := len(a)) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")


# Example Usage Case 5
# Before Python 3.8
numbers = [2, 8, 0, 1, 1, 9, 7, 7]
num_length = len(numbers)
num_sum = sum(numbers)
description = {
    "length": num_length,
    "sum": num_sum,
    "mean": num_sum / num_length,
}

print(description)  # {'length': 8, 'sum': 35, 'mean': 4.375}

# With Walrus Operator
numbers = [2, 8, 0, 1, 1, 9, 7, 7]
description = {
    "length": (
        num_length := len(numbers)
    ),  # Here we are initializing and using both at the same time
    "sum": (num_sum := sum(numbers)),
    "mean": num_sum / num_length,
}
print(description)  # {'length': 8, 'sum': 35, 'mean': 4.375}
