#!/usr/bin/python
"""
Purpose: timeit module
"""
import timeit

print("\n timeit.timeit")
print(
    timeit.timeit('"-".join(str(n) for n in range(10))', number=10_000)
)  # 0.02176020003389567
print(timeit.timeit('"-".join([str(n) for n in range(10)])', number=10000))
print(timeit.timeit('"-".join(map(str, range(10)))', number=10000))
print(timeit.timeit(lambda: "-".join(map(str, range(10))), number=10000))

print("\n timeit.repeat")
print(timeit.repeat('"-".join(str(n) for n in range(10))', number=10000))
print(timeit.repeat('"-".join([str(n) for n in range(10)])', number=10000))
print(timeit.repeat('"-".join(map(str, range(10)))', number=10000))
print(timeit.repeat(lambda: "-".join(map(str, range(10))), number=10000))

print("\n timeit.Timer")
# By default, timeit() temporarily turns off garbage
# collection during the timing.
print(timeit.Timer("for i in range(10): oct(i)", "gc.enable()").timeit())
