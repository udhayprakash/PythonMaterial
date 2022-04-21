#!/usr/bin/python
"""
Purpose: Dunder Methods
"""


class LazyDB:
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = 'Value for %s' % name
        setattr(self, name, value)
        return value

data = LazyDB()
print('Before:', data.__dict__)  # vars(data)
print('foo   :', data.foo)
print('After :', data.__dict__)
print()

# -------------
class LoggingLazyDB(LazyDB):
    def __getattr__(self, name):
        print('Called __getattr__(%s)' % name)
        # return LazyDB.__getattr__(self, name)
        return super().__getattr__(name)

    def __delattr__(self, attribute):
        print('Deleting the given attribute')


data = LoggingLazyDB()
print('exists:', data.exists)
print('foo   :', data.foo)

del data.foo
print(vars(data))
