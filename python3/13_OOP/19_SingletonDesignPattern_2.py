#!/usr/bin/python
"""
Purpose: To create a class with singleton design pattern 
    It means, If an instance of that class is already created, 
    Instead of creating new instance, make use of already created instance

	Or NOT allowing new instance creation
"""

class Singleton:
	__single = None

	def __init__(self):
		if Singleton.__single:
			raise Singleton.__single
		Singleton.__single = self

s = Singleton()
print(s)
# print(dir(s))

d = Singleton()
print(d)
#print dir(d)
