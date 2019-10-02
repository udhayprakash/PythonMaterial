#!/usr/bin/python
"""
Purpose: Generators
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
    print(f'res1:{res1} type(res1):{type(res1)}')
except StopIteration as ex:
    print(repr(ex))

for ech in result:
    print(ech)

print('\n After Re-initializing')
result = my_generator()
for ech in result:
    print(ech)
