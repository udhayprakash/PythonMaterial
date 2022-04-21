#!/usr/bin/python3
"""
Purpose: closure example demo
"""


def outer(num1):
    num3 = 30

    def hello_world():
        print("Hello world")

    def wrapper(num2):  # closure function
        result = num1 + num2 + num3
        return result

    print(f"{hello_world.__closure__ =}")
    print(f"{wrapper.__closure__ =}")

    return wrapper


outer_result = outer(10)
print(f"{type(outer_result)} {outer_result}")

print(f"{outer.__closure__ =}")

# <function outer.<locals>.hello_world
