#!/usr/bin/python
"""
Purpose:

Iterator objects
    - iterator is an immutable, disposable and lazy object
    - designed for builtin iterable objects
    - can't be indexed
    - stores the state
    - used for large data handling
    - values can be retrieved by 
        - .next() in python 2.x 
            .__next__() in pyton 3.x
        - applying for loop
"""

# vegetables = ['carrot', 'brinjol', 'beetroot']
# print("vegetables      :", vegetables)
# print("type(vegetables):", type(vegetables))
# print("vegetables[1]", vegetables[1])

# vegetables_iter = iter(vegetables)
# print("\n\nvegetables_iter      :", vegetables_iter)
# print("type(vegetables_iter):", type(vegetables_iter))
# # print("vegetables_iter[1]", vegetables_iter[1])
# print(dir(vegetables_iter))

# print
# # print(vegetables_iter.next())  # AttributeError: 'list_iterator' object has no attribute 'next'
# print(vegetables_iter.__next__())  
# print(next(vegetables_iter))

# print(next(vegetables_iter))
# # print(vegetables_iter.__next__()) 

# try:
#     print(vegetables_iter.__next__()) 
# except StopIteration as ex:
#     print(repr(ex))

# print('looping with for')
# # Iterator objects are disposable objects
# for each_vegetable in vegetables_iter:
#     print("each_vegetable", each_vegetable)

# # reassign
# vegetables_iter = iter(vegetables)
# for each_vegetable in vegetables_iter:
#     print("each_vegetable", each_vegetable)

# # reassign
# vegetables_iter = iter(vegetables)
# print('vegetables_iter', vegetables_iter)
# print('list(vegetables_iter)', list(vegetables_iter))
# print('\n')

veto_countries = ('USA', 'UK', 'France', 'China', 'Russia')
print("veto_countries      :", veto_countries)
print("type(veto_countries):", type(veto_countries))
print("veto_countries[1]", veto_countries[1])


veto_countries_iter = iter(veto_countries)
print("veto_countries_iter      :", veto_countries_iter)
print("type(veto_countries_iter):", type(veto_countries_iter))
# print("veto_countries_iter[1]", veto_countries_iter[1])

# print(dir(veto_countries_iter))

# print(veto_countries_iter.next)
# print(callable(veto_countries_iter.next))

print(next(veto_countries_iter))
print(next(veto_countries_iter))
print(next(veto_countries_iter))
print(next(veto_countries_iter))
print(next(veto_countries_iter))
print(next(veto_countries_iter)) # StopIteration

# Iterator objects are disposable objects
# for each_country in veto_countries_iter:
#     print("each_country", each_country)

# reassign
# veto_countries_iter = iter(veto_countries)
# for each_country in vegetables_iter:
#     print("each_country", each_country)

# print('\n')


# # set - set iterator
# # dictionary - dictionary key iterator
