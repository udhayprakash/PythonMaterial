"""
Purpose: Imutable values
"""
import logging

logging.basicConfig(level=logging.DEBUG)


class MyClass:
    def __init__(self, getter_func):
        logging.debug("In __init__ method")
        self.getter_func = getter_func
        self.setter_func = None

    def __get__(self, obj, cls):
        logging.debug("In __get__ method")
        return self.getter_func(obj)

    def setter(self, setter_func):
        logging.debug("In setter method")
        self.setter_func = setter_func

    def __set__(self, obj, value):
        logging.debug("In __set__ method")
        if self.setter_func is None:
            raise RuntimeError("This attribute cannot be set!")

        self.setter_func(obj, value)


def hello():
    return "Hello world"


val1 = MyClass(hello)

print(f"{val1.getter_func =}")


# __get__ and __getattr__


class C:
    def __init__(self) -> None:
        self._x = 42

    @my_property
    def x(self):
        return self._x

    @x.setter
    def set_x(self, new_value):
        if new_value < self._x:
            raise ValueError("new value must be bigger than old one")

        self._x = new_value


c = C()
print(c.x)  # 42
c.x += 1
print(c.x)  # 43
