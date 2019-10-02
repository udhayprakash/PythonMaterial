#!/usr/bin/python
"""
Purpose: To create a class with singleton design pattern 
    It means, If an instance of that class is already created, 
    Instead of creating new instance, make use of already created instance

	Or NOT allowing new instance creation
"""


def singleton(myClass):
    instances = {}

    def getInstance(*args, **kwargs):
        if myClass not in instances:
            instances[myClass] = myClass(*args, **kwargs)
        return instances[myClass]

    return getInstance


@singleton
class TestClass(object):
    pass


x1 = TestClass()
print(x1, id(x1))

x2 = TestClass()
print(x2, id(x2))

# class Singleton(object):
#     """Use to create a singleton"""
#     def __new__(cls, *args, **kwds):
#         """
#         >>> s = Singleton()
#         >>> p = Singleton()
#         >>> id(s) == id(p)
#         True
#         """
#         self = "__self__"
#         if not hasattr(cls, self):
#             instance = object.__new__(cls)
#             instance.init(*args, **kwds)
#             setattr(cls, self, instance)
#         return getattr(cls, self)

#     def init(self, *args, **kwds):
#         pass

# s1 = Singleton()
# p1 = Singleton()
# print(s1, p1)

# print(id(s1), id(p1))
