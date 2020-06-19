import functools

@functools.lru_cache(maxsize=4)
def fibonacci(num):
    print(f"Calculating fibonacci({num})")
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


if __name__ =='__main__':
    fibonacci(2)
    print()

    fibonacci(4)
    print()

    fibonacci(8)
    print()

    print(f'\n{fibonacci.cache_info() =}')