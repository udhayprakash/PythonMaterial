from timeit import timeit

print(timeit("factorial(999)", "from math import factorial", number=10))


from math import factorial
print(timeit(lambda: factorial(999), number=10))