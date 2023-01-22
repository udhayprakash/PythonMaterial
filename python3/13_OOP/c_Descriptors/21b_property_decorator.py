class my_property:
    def __init__(self, getter_func):
        self.getter_func = getter_func
        self.setter_func = None

    def __get__(self, obj, cls):
        return self.getter_func(obj)

    def setter(self, setter_func):
        self.setter_func = setter_func

    def __set__(self, obj, value):
        if self.setter_func is None:
            raise RuntimeError("This attribute cannot be set!")

        self.setter_func(obj, value)


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
