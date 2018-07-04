#!/usr/bin/python

__author__ = 'udhay prakash'



def double(x):
    return x*2

print double(12)

db = lambda x:x*2
print db(12)

print map(double, range(6))   # applying function for a list
print map(db, range(6))       # applying lambda for a list

print '-'*80

def addition(m,n):
    return m+n

print addition(23, 10)

addn = lambda p,q:p+q

print addn(23, 10)

print map(addition, range(6), range(6))   # applying function for a list
print map(addn, range(6), range(6))       # applying lambda for a list

print '-'*80
print 'with expr'
print map(lambda x: x**2 -2*x+ 12, range(5))
print map(lambda x: x*2, range(5))
print map(lambda x: x, [(1, 2), (3,4), (5,6)])
print map(lambda x: x[0], [(1, 2), (3,4), (5,6)])
print map(lambda x: x[1], [(1, 2), (3,4), (5,6)])

print '-'*80
def printSquares(x):
    for i in range(x):
        print i,":", i**2

printSquares(7)


print [(x,x**2)  for x in range(7)]
#print [(x:x**2)  for x in range(7)]


#print map([lambda x:x**2  for x in range(7)])

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
print map( lambda a, b: a * b, [1, 2, 3, 4] , [1, 2, 3, 4])
print reduce( (lambda a, b: a * b), [1, 2, 3, 4] )   # results in 1*2*3*4

print reduce( (lambda a, b: a ** b), [1, 2, 3, 4] )   # results in 1**2**3**4; anything to the power of 1 results in 1
print reduce( (lambda a, b: a ** b), [2, 3, 4] )    # results in 2**3**4




string = 'I am confident about my Success'
list = string.split(' ')
print list

print reduce(lambda a,b:a+' ' + b, list)

print '='*80
"""
### Recursive functions


```
def funcName(<input paramaters>):
    <some logic>
    return funcName(<input parameters>)
```

Recursion is a programming technique in which a call to a function results in another call to that same function.
Iteration is calling an object, and moving over it.


"""

# __Problem 1:__ Return the fibonacci series (0, 1, 1, 2, 3, 5, 8) using recursions

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+ fib(n-2)

# 5th element    # fib(4)+fib(3)
                 # fib(4) -> fib(3)+fib(2);
                        # fib(3) -> fib(2)+fib(1)
                                    # fib(2) -> fib(1)+ fib(0) = 1+ 0
                 #             fib ...
print fib(5)

print '='*80
# factorial(5) = 5*4*3*2*1 =


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print factorial(0)
print factorial(1)
print factorial(3)
print factorial(5)

print '='*80

# infinite loop
'''
def display(name):
    print name
    return display(name)

display('Michel')

#global noOfRecursions
noOfRecursions = 0

def loop(noOfRecursions):             # Infinite loop
    print 'Hi! I am in Loop '
    noOfRecursions+=1              # to get the count of number of recursions occurred
    print 'This is Loop %d'%noOfRecursions
    return loop(noOfRecursions)

loop(5)

'''



# Infinite loop between these functions  --- Mutual recursion
def func1():
    print 'I am in function 1 .'
    return func2()

def func2():
    print 'I am in function 2 .'
    return func1()

func1()

'''
**NOTE :**
- Python doesnot have Tail Call optimization(TCO), to handle the recursive functions.
- It is very difficult to add TCO to python, as it is a dynamic language.
'''
