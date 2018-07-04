Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:19:22) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for i in 2:
	print i

	

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    for i in 2:
TypeError: 'int' object is not iterable
>>> 
>>> 
>>> # iterable objects: string, list, tuple, dictionary, set, frozenset, xrange

>>> 
>>> # iterator is an immutable, disposable and lazy object
>>> 
>>> 
>>> d = {'a': 12, 'c': 34, 'b': 23}
>>> d.values()
[12, 34, 23]
>>> d.keys()
['a', 'c', 'b']
>>> di = iter(d)
>>> diV = iter(d.values())
>>> 
>>> type(di)
<type 'dictionary-keyiterator'>
>>> type(diV)
<type 'listiterator'>
>>> 
>>> 
>>> iter(2)

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    iter(2)
TypeError: 'int' object is not iterable
>>> # CONCLUSION: UNITERABLES CAN'T BE CONVERTED TO ITERATORS
>>> 
>>> 
>>> 
>>> 
>>> def func(3):
	
SyntaxError: invalid syntax
>>> 
============ RESTART: C:/Users/PRAUD01/Documents/generator_ex.py ============
0
1
2
3
4
None
0
<generator object func2 at 0x02264D78>
>>> 
============ RESTART: C:/Users/PRAUD01/Documents/generator_ex.py ============
func(5)  0
1
2
3
4
None
func1(5)  0
func2(5)  <generator object func2 at 0x02BDFC10>
>>> 
============ RESTART: C:/Users/PRAUD01/Documents/generator_ex.py ============
func(5)  0
1
2
3
4
None
func1(5)  0
func2(5)  <generator object func2 at 0x029BF8F0>
<generator object func2 at 0x029EFD28>
0
>>> 
============ RESTART: C:/Users/PRAUD01/Documents/generator_ex.py ============
func(5)  0
1
2
3
4
None
func1(5)  0
func2(5)  <generator object func2 at 0x02A5FD28>
<generator object func2 at 0x02A2F8F0>
0
1
>>> 
============ RESTART: C:/Users/PRAUD01/Documents/generator_ex.py ============
func(5)  0
1
2
3
4
None
func1(5)  0
func2(5)  <generator object func2 at 0x02144CB0>
<generator object func2 at 0x0298FE40>
0
5
2
3
4
>>> 
============ RESTART: C:/Users/PRAUD01/Documents/generator_ex.py ============
func(5)  0
1
2
3
4
None
func1(5)  0
func2(5)  <generator object func2 at 0x02A3FC10>
<generator object func2 at 0x021D4D78>
0
5
2
3
4
finally

Traceback (most recent call last):
  File "C:/Users/PRAUD01/Documents/generator_ex.py", line 30, in <module>
    print 'finally', f5.next()
StopIteration
>>> 
============ RESTART: C:/Users/PRAUD01/Documents/generator_ex.py ============
func(5)  0
1
2
3
4
None
func1(5)  0
func2(5)  <generator object func2 at 0x02A5FC10>
<generator object func2 at 0x02A5FC60>
0
5
2
3
4
>>> 
