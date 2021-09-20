#!/usr/bin/python3
"""
Purpose: Generators

    range(0, 100000, 2) -> 0
    range(2, 100000, 2) -> 2
    range(4, 100000, 2) -> 4
    range(6, 100000, 2) -> 6
    ....

return is the last statement to execute in any function

yield - keyword in python
    If yield is placed within function definition, 
    it becomes generator

PEP8 - dont use both return & yield in same function

"""
def my_generator():
    print(' I am in the function')
    yield 111
    print('yielding 222')
    yield 222
    print('yielding 333')
    yield 333
    print('yielding 444')
    yield 444
    return "No MORE VALUES"

result = my_generator()
print(type(result), result)

# Execution starts below
res1 = next(result)  # 111
print(f'res1:{res1} type(res1):{type(res1)}')

res1 = next(result)  # 222
print(f'res1:{res1} type(res1):{type(res1)}')

res1 = next(result)  # 333
print(f'res1:{res1} type(res1):{type(res1)}')

res1 = next(result)  # 444
print(f'res1:{res1} type(res1):{type(res1)}')

try:
    res1 = next(result)  # StopIteration
except StopIteration as ex:
    print(repr(ex))


for ech in result:
    print(ech)


print('\n After Re-initializing')
result = my_generator()
for ech in result:
    print(ech)


result = my_generator()
print('\n', list(result))   #  [111, 222, 333, 444]

result = my_generator()
print('\n', tuple(result))  # (111, 222, 333, 444)

result = my_generator()
print('\n', set(result))   # {111, 222, 333, 444}

result = my_generator()
print('\n', str(result))   #  <generator object my_generator at 0x000002CC22552F20>
