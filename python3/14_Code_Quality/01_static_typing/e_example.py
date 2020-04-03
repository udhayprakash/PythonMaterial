from typing import Iterator


# Using Dynamic typing
def fib(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


# Using Static Typing
def fib1(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    print(list(fib(10)))
    print(list(fib1(10)))
