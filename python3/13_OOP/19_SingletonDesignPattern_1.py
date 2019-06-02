#!/usr/bin/python
"""
Purpose: To create a class with singleton design pattern 
    It means, If an instance of that class is already created, 
    Instead of creating new instance, make use of already created instance
"""

class Logger(object):
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, '_logger'):
			cls._logger = super(Logger, cls).__new__(cls, *args, **kwargs)
		return cls._logger 

l = Logger()
print(l)
# print(dir(l))

l1 = Logger()
print(l1)
# print(dir(l1))
print(id(l), id(l1))
