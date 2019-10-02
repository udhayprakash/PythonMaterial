#!/usr/bin/python

from os import system

# clear screen 
system('cls')


class LazyDB:
    def __init__(self):
        self.exists = 5

    def __getattr__(self, name):
        value = 'Value for %s' % name
        setattr(self, name, value)
        return value


data = LazyDB()
print('Before:', data.__dict__)
print('foo   :', data.foo)
print('After :', data.__dict__)

print('-' * 40, '\n' * 2)


class LoggingLazyDB(LazyDB):
    def __getattr__(self, name):
        print('Called __getattr__(%s)' % name)
        return super().__getattr__(name)


data = LoggingLazyDB()
print('exists:', data.exists)
print('foo   :', data.foo)
print('foo   :', data.foo)
