from functools import wraps


def decorator(arg1, arg2):

    def inner_function(function):

        @wraps(function)
        def wrapper(*args, **kwargs):
            print(f'Arguments passed to decorator are {arg1} and{arg2}')
            print(f'Function arguments are {args}')
            function(*args, **kwargs)
        return wrapper

    return inner_function


@decorator('arg1', 'arg2')
def print_args(*args):
    for arg in args:
        print(arg)


print_args(1, 2, 3)
