class ReadOnlyDescriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, obj, type=None):
        return self.value


class MyClass:
    x = ReadOnlyDescriptor(10)


obj = MyClass()
print(obj.x)  # prints 10
obj.x = 20  # Raises AttributeError
print(obj.x)  # prints 10
print()


# -----------------------------------
class SubClass:
    def __init__(self) -> None:
        self.__secret = "secret"

    def __get__(self, obj, type):
        return self.__secret

    def __set__(self, obj, val):
        self.__secret = val


class SuperClass:
    val = SubClass()


obj1 = SuperClass()
obj1.val = "not secret"
print(f"{obj1.val = }")

obj2 = SuperClass()
print(f"{obj2.val = }")
