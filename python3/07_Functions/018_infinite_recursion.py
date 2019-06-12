# infinite loop
import sys

# def display(name):
#     print(name)
#     return display(name)

# display('Udhay')


# To get the stack depth - platform dependent
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())


global noOfRecursions
noOfRecursions = 0

# Infinite loop
def loop(noOfRecursions):             
    # print('Hi! I am in Loop ')
    # to get the count of number of recursions occurred
    noOfRecursions+=1              
    print('This is Loop %d'%noOfRecursions)
    return loop(noOfRecursions)

loop(noOfRecursions)

# # mutual recursion
# def func1():
#     print('func1')
#     return func2()

# def func2():
#     print('func2')
#     return func1()

# func1()