#!/usr/bin/python
"""
Purpose:

Iterator objects
    - designed for builtin iterable objects
    - disposable
    - can't be indexed
    - stores the state
    - used for large data handling
"""
from __future__ import print_function

vegetables = ['carrot', 'brinjol', 'beetroot']
print("vegetables      :", vegetables)
print("type(vegetables):", type(vegetables))
print("vegetables[1]", vegetables[1])

vegetables_iter = iter(vegetables)
print("\n\nvegetables_iter      :", vegetables_iter)
print("type(vegetables_iter):", type(vegetables_iter))
# print("vegetables_iter[1]", vegetables_iter[1])
print(dir(vegetables_iter))

print
print(vegetables_iter.next)
print(callable(vegetables_iter.next))

print(vegetables_iter.next())
print(next(vegetables_iter))
print(vegetables_iter.next())

try:
    print(vegetables_iter.next()) # StopIteration
except:
    pass

print('looping with for')
# Iterator objects are disposable objects
for each_vegetable in vegetables_iter:
    print("each_vegetable", each_vegetable)

# reassign
vegetables_iter = iter(vegetables)
for each_vegetable in vegetables_iter:
    print("each_vegetable", each_vegetable)

print('\n')

veto_countries = ('USA', 'UK', 'France', 'China', 'Russia')
print("veto_countries      :", veto_countries)
print("type(veto_countries):", type(veto_countries))
print("veto_countries[1]", veto_countries[1])


veto_countries_iter = iter(veto_countries)
print("veto_countries_iter      :", veto_countries_iter)
print("type(veto_countries_iter):", type(veto_countries_iter))
# print("veto_countries_iter[1]", veto_countries_iter[1])

print(dir(veto_countries_iter))

print(veto_countries_iter.next)
print(callable(veto_countries_iter.next))

print(veto_countries_iter.next())
print(veto_countries_iter.next())
print(veto_countries_iter.next())
print(veto_countries_iter.next()) # StopIteration

# Iterator objects are disposable objects
for each_country in veto_countries_iter:
    print("each_country", each_country)

# reassign
veto_countries_iter = iter(veto_countries)
for each_country in vegetables_iter:
    print("each_country", each_country)

print('\n')


# # set - set iterator
# # dictionary - dictionary key iterator
