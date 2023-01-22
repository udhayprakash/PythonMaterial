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
