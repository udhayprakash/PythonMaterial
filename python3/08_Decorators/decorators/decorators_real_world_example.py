import warnings


def deprecated(func):
    def new_func(*args, **kwargs):
        warnings.warn("This function is old", DeprecationWarning, 2)
        return func(*args, **kwargs)

    return new_func


@deprecated
def i_am_old(foo, bar):
    return foo, bar


# def change_doc(docstring):
#    def decorator(func):
#        func.__doc__ = docstring
#        return func
#    return decorator

# @change_doc("My super-new docstring")
# def foo(bar):
#    """ My old docstring """
#    return bar

# foo = change_doc("My super-new docstring")(foo)

if __name__ == "__main__":
    # print foo.__doc__
    print(i_am_old(42, "Answer"))
