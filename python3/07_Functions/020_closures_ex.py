#!/usr/bin/python
"""
Purpose: closure example demo
"""
def outer(num1):
    num3 = 30

    def hello_world():
        print('Hello world')

    def wrapper(num2):
        result = num1 + num2 + num3
        return result

    print('hello_world.__closure__', hello_world.__closure__)
    print('wrapper.__closure__    ', wrapper.__closure__)
    return wrapper


outer_result = outer(10)


print('outer_result', outer_result)
print('outer_result()', outer_result(20))

# print(num3)

# print(dir(outer))
print('outer.__closure__', outer.__closure__)
