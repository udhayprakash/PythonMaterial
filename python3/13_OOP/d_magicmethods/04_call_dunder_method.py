"""
Purpose: __call__ method importance
"""


class MyClass:
    def __init__(self):
        print("Constructor is called")

    def __str__(self):
        return "This is instance of MyClass"

    def __call__(self, *args, **kwargs):
        """Used to make the instance callable"""
        print("This is called")


m = MyClass()
print(m)  # __str__

print(f"callable(m):{callable(m)}")
m()


# ------------------------------------------------
import functools


class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@CountCalls
def say_whee():
    print("\t\t\tWhee!")


if __name__ == "__main__":
    say_whee()
    say_whee()
    say_whee()
