import functools

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat


@repeat(num_times=4)
def greet(name):
    print(f'Hello {name}')

if __name__ =='__main__':
    greet('World')
