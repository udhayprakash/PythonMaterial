#!/usr/bin/python

__author__ = 'udhay prakash'

def printSquares(x):
    for i in range(x):
        print i,":", i**2

printSquares(7)

print map(lambda x:x**2, range(7))

print '='*80
print map(lambda x:x%2 == 0, range(5))    # result is boolean
print filter(lambda x:x%2 == 0, range(5)) # result is elements, which are True

print map(lambda x:x%2 != 0, range(5))    # result is boolean
print filter(lambda x:x%2 != 0, range(5)) # result is elements, which are True

print '+'*80
# zip vs map

print zip('Python', 'Python')
print map(None, 'Python', 'Python')

print zip('Python', 'Python123')
print map(None, 'Python', 'Python123')


print zip(xrange(len('python')), 'Python')


print '='*80
print map(    lambda a, b: a * b, [1, 2, 3, 4] , [1, 2, 3, 4])
print reduce( lambda a, b: a * b, [1, 2, 3, 4] )   # results in 1*2*3*4

print reduce( (lambda a, b: a ** b), [1, 2, 3, 4] )   # results in 1**2**3**4; anything to the power of 1 results in 1
print reduce( (lambda a, b: a ** b), [2, 3, 4] )    # results in 2**3**4




string = 'I am confident about my Success'
list_of_content = string.split(' ')
print list_of_content

print ' '.join(list_of_content)
print reduce(lambda a,b:a + ' '+ b, list_of_content)
