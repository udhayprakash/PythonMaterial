# decorator1.py
# simple example of decorators


def changeDoc(func):
    func.__doc__ = "This is new docstring"
    return func


@changeDoc
def foo(bar):
    """My old docstring"""
    return bar


if __name__ == "__main__":
    print(foo.__doc__)


# decorator2.py
# simple example of decorators


def changeDoc(docstring):
    def decorator(func):
        func.__doc__ = docstring
        return func

    return decorator


# @changeDoc("My super-new docstring")
def foo(bar):
    """My old docstring"""
    return bar


foo = changeDoc("My super-new docstring")(foo)
if __name__ == "__main__":
    print(foo.__doc__)


# decorator3.py
# simple example of decorators
import warnings


def deprecated(func):
    def newFunc(*args, **kwargs):
        warnings.warn("This function is old", DeprecationWarning, 2)
        return func(*args, **kwargs)

    return newFunc


@deprecated
def iAmOld(foo, bar):
    return foo, bar


def changeDoc(docstring):
    def decorator(func):
        func.__doc__ = docstring
        return func

    return decorator


# @changeDoc("My super-new docstring")
def foo(bar):
    """My old docstring"""
    return bar


foo = changeDoc("My super-new docstring")(foo)
if __name__ == "__main__":
    # print foo.__doc__
    iAmOld(28, "Answer")
