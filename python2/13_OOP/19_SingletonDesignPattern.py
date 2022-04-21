class Logger(object):
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, '_logger'):
			cls._logger = super(Logger, cls).__new__(cls, *args, **kwargs)
		return cls._logger

l = Logger()
print l
print dir(l)

l1 = Logger()
print l1
print dir(l1)
print id(l), id(l1)
print '='*100

class Singleton:
	__single = None
	def __init__(self):
		if Singleton.__single:
			raise Singleton.__single
		Singleton.__single = self

s = Singleton()
print s
print dir(s)

#d = Singleton()
#print d
#print dir(d)

'''
child = Child('Monty')
junior = Handle(Junior)
print junior.name()

single = Handle()
print single
'''

class Singleton(object):
    """Use to create a singleton"""
    def __new__(cls, *args, **kwds):
        """
        >>> s = Singleton()
        >>> p = Singleton()
        >>> id(s) == id(p)
        True
        """
        self = '__self__'
        if not hasattr(cls, self):
            instance = object.__new__(cls)
            instance.init(*args, **kwds)
            setattr(cls, self, instance)
        return getattr(cls, self)

    def init(self, *args, **kwds):
        pass

s1 = Singleton()
p1 = Singleton()
print s1, p1

print id(s1), id(p1)

print '='*100

class Myclass:
    pass

_singleton = None

def get_singleton(cls = Myclass):
    global _singleton
    if _singleton is None:
        _singleton = cls()
    return _singleton

a = get_singleton()
print a
b = get_singleton()
print b
print id(a), id(b)

print '+'*100

class MySingleton(object):
    _instance = None
    def __new__(self):
        if not self._instance:
            self._instance = super(MySingleton, self).__new__(self)
            self.y = 10
        return self._instance

x = MySingleton()
print x.y

z = MySingleton()
print z.y


print id(x), id(z)


print '*'*100

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

print x1, id(x1)
