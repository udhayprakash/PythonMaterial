def function_logger(actual_function):
    def wrapper(*args, **kwargs):
        function_name = actual_function.func_code.co_name
        print("Entering {} with arguments {} and {}" \
            .format(function_name, args, kwargs))
        temp = actual_function(*args, **kwargs)
        print("Leaving  {} with {}, when arguments were {} and {}" \
            .format(function_name, temp, args, kwargs))
        return temp
    return wrapper

@function_logger
def function(*args, **kwargs):
    return args, kwargs

    
function(1)
function(1, default = 1)