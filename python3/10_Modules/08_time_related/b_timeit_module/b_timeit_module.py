#!/usr/bin/python
"""
Purpose: timeit module
"""
import time
import timeit

LOGIC = '"-".join(str(n) for n in range(10))'

start_time = time.perf_counter_ns()
res = eval(LOGIC)
print(res)
print(f"TIME TAKEN: {time.perf_counter_ns() - start_time}")
print()

print("\n timeit.timeit")
print(timeit.timeit(LOGIC))
print(timeit.timeit(LOGIC, number=10_000))
print(timeit.timeit('"-".join([str(n) for n in range(10)])', number=10000))
print(timeit.timeit('"-".join(map(str, range(10)))', number=10000))
print(timeit.timeit(lambda: "-".join(map(str, range(10))), number=10000))

print("\n timeit.repeat")
print(timeit.repeat('"-".join(str(n) for n in range(10))', number=10000))
print(timeit.repeat('"-".join([str(n) for n in range(10)])', number=10000))
print(timeit.repeat('"-".join(map(str, range(10)))', number=10000))
print(timeit.repeat(lambda: "-".join(map(str, range(10))), number=10000, repeat=3))

print("\n timeit.Timer")
# By default, timeit() temporarily turns off garbage
# collection during the timing.
print(timeit.Timer("for i in range(10): oct(i)", "gc.enable()").timeit())
