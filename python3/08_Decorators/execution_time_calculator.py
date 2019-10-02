import time


def function_logger(func):
    def wrapper(*args, **kwargs):
        start_time, temp = time.time(), func(*args, **kwargs)
        elasped = time.time() - start_time
        print(("{} took {:.3f} sec, returning {}, arguments {} and {}" \
               .format(func.__code__.co_name, elasped, temp, args, kwargs)))
        return temp

    return wrapper


@function_logger
def function(*args, **kwargs):
    for i in range(int(args[0])):
        for j in range(int(args[0])):
            pass


function(1000)
