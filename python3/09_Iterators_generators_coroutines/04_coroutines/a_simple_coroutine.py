# -*- coding: utf-8 -*-
from __future__ import print_function
"""
• Coroutines are not related to iteration

- generators are data producers
- coroutines are data consumers

- Coroutines consume values using a (yield)
"""

def coro():
    hello = yield "Hello"
    yield hello                   # resulted with c.send("World")
 
 
c = coro()
print('c', c)

# All coroutines must be "primed" by first calling .next() (or send(None))
print(next(c))
print(c.send("World"))

try:
    c.throw(RuntimeError,"I am throwing exception")
except RuntimeError as ex:
    print(ex)

# closing(shutdown) a coroutine
c.close()
# garbage collection too calls .close() 

# close() can be catched by GeneratorExit Exception