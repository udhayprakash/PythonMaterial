#!/usr/bin/python
"""
Purpose: Functions will math operations
    - factorial
    - fibonacci
"""


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n + 1):
        series.append(a)
        a, b = b, a + b
    return series


if __name__ == "__main__":
    print(f"{factorial(10) =}")
    print(f"{fibonacci(10) =}")
