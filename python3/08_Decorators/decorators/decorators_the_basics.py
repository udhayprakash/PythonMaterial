def change_doc(docstring):
    def decorator(func):
        func.__doc__ = docstring
        return func

    return decorator


# @change_doc("My super-new docstring")
def foo(bar):
    """My old docstring"""
    return bar


foo = change_doc("My super-new docstring")(foo)

if __name__ == "__main__":
    print(foo.__doc__)
