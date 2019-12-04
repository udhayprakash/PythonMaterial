#!usr/bin/env python

# import numpy
import numpy as np  # aliasing the import

from numpy import *   # Another way of importing
from numpy import array

'''
Array is similar to list in python, execept that 
every element of an array must be of the same type,
typically a numeric type like FLOAT or INT.
'''

# Integer type array
a = np.array([1, 4, 5, 8, ])  # default type is Integer.

print("a=", a)
print("type(a)=", type(a))
print("type(a[2])=", type(a[2]))

print("a[3]=", a[3])
print("a[:2]=", a[:2])

a[0] = 5.
print("after assignment, a=", a)
print("type(a[0])=", type(a[0]))
# -------------------------------------------
# Float type array
a = np.array([1, 4, 5, 8, ], float)

print("a=", a)
print("type(a)=", type(a))
print("type(a[2])=", type(a[2]))

print("a[:2]=", a[:2])
print("a[3]=", a[3])
# -------------------------------------------

a[0] = 5
print("after assignment, a=", a)
print("type(a[0])=", type(a[0]))

'''
Arrays can also be multi-dimensional.
[
    [1. 2. 3.]
    [4. 5. 6.]
]
'''

a = np.array([[1, 2, 3], [4, 5, 6]], float)
print("a=", a)
print("a[0,0]=", a[0, 0])
print("a[0,1]=", a[0, 1])

'''
Array slicing works with multiple dimensions in the same way, as for lists
'''
a = np.array([[1, 2, 3], [4, 5, 6]], float)

print("a[1,:]=", a[1, :])
print("a[:,2]=", a[:, 2])
print("a[-1:, -2:]=", a[-1:, -2:])

print('a.shape=', a.shape)  # results in the dimensions of that array

'''
dtype property tells you what type of values are stored by the array.
'''

print("a.dtype=", a.dtype)
a = np.array([[1, 2, 3], [4, 5, 6]], float)
print("a=", a)
print("len(a)=", len(a))

''' in operator is used to test the presence of an element in an array. '''
print("2 in a ", 2 in a)
print("0 in a ", 0 in a)

''' Arrays can be reshaped using TUPLES that specify new dimensions. '''
a = np.array(range(10), float)

print("a=", a)
print("a.shape = ", a.shape)
a = a.reshape((5, 2))  # possible reshapes will be the multiples of the total no. of elements.
print("a=", a)
print("a.shape = ", a.shape)
print("Notice that reshape function creates a new array and doesn't itself modify the original array.")

''' Python's name binding approach applies to arrays,also. '''
a = np.array([1, 2, 3], float)
b = a
c = a.copy()
a[0] = 0
print("a= ", a)
print("b= ", b)
print("c= ", c)
# try hard copy and deepcopy problem with arrays, as an assignment.

''' Lists can also be created from arrays. '''
a = np.array([1, 2, 3], float)
print("a= ", a)
print("a.tolist()   =", a.tolist())
print('list(a)      = ', list(a))

a = np.array([[1, 2, 3], [4, 5, 6]], float)
print("a= ", a)
print("a.tolist() =", a.tolist())
print('list(a) = ', list(a))

'''raw data to binary conversion'''
a = np.array([[1, 2, 3], [4, 5, 6]], float)
print("a=", a)
s = a.tostring()
print("s=", s)
a1 = np.fromstring(s)
print("a1 = ", a1)

''' The complete array can be filled with a single value. '''
a = np.array([[1, 2, 3], [4, 5, 6]], float)
print("a= ", a)
a.fill(99)
print("a= ", a)

# ''' Transposed versions of arrays can also be generated, which will create a new array with the final two axes switched.'''
# a = np.array(range(6), float).reshape((2, 3))
# print("a=", a)
# print("a.transpose() =", a.transpose())
#
# ''' One-dimensional versions of multi-dimensional arrays can be generated with flatten '''
# a = np.array(list(range(6)), float).reshape((2, 3))
# print("a=", a)
# print("a.flatten() =", a.flatten())
# print("a.reshape((6,)) =", a.reshape((6,)))
#
# ''' Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined. '''
# a = np.array([1, 2], float)
# b = np.array([3, 4, 5, 6], float)
# c = np.array([7, 8, 9], float)
#
# print("np.concatenate((a,b,c))", np.concatenate((a, b, c)))
#
# ''' For multi-dimensional arrays, it is possible to specify the axis along which multiple arrays can be concatenated. '''
# a = np.array([[1, 2], [3, 4]], float)
# b = np.array([[5, 6], [7, 8]], float)
# print("np.concatenate((a,b)) =", np.concatenate((a, b)))
# print("np.concatenate((a,b), axis = 0) =", np.concatenate((a, b), axis=0))
# print("np.concatenate((a,b), axis = 1) =", np.concatenate((a, b), axis=1))
#
# a = np.array([1, 2, 3], float)
# print("a = ", a)
# print("a[:, np.newaxis]\n", a[:, np.newaxis])
# print("a[:, np.newaxis].shape \n", a[:, np.newaxis].shape)
#
# print("b = ", b)
# print("b[np.newaxis, :]\n", b[np.newaxis, :])
# print("b[np.newaxis, :].shape \n", b[np.newaxis, :].shape)
#
# # Other ways to create arrays
# ''' arange function is similar to the range function but returns an array. '''
# print("np.arange(5, dtype = float)  ", np.arange(5, dtype=float))
# print("np.arange(1,6,2, dtype = int)", np.arange(1, 6, 2, dtype=int))
#
# """ Ones and Zeros creates 1's and 0's corrrespondingly, OF THE TYPE SPECIFIED. """
# print("np.ones((2,3), dtype = float) ", np.ones((2, 3), dtype=float))
# print("np.zeros(7, dtype = int) ", np.zeros(7, dtype=int))
#
# """ Ones_like and Zeros_like creates 1's and 0's corrrespondingly, OF THE SAME dimensions and type of an existing one. """
# a = np.array([[1, 2, 3], [4, 5, 6]], float)
# print("np.zeros_like(a) ", np.zeros_like(a))
# print("np.ones_like(a)", np.ones_like(a))
#
# '''For creating an identity matrix of a given size, np.identity() can be used. '''
# print("np.identity(4, dtype = float)\n", np.identity(4, dtype=float))
#
# ''' For creating an unit matrix, eye function can be used. '''
# print("np.eye(4, k=1, dtype = float)\n", np.eye(4, k=1, dtype=float))
#
# print("np.eye(4, k= 81, dtype = float)", np.eye(4, k=1, dtype=float))
#
# '''
# Array Arithmetics:
# As standard mathematical operations work on element-by-element basis, the array (under operation) should be of the same
# dimensions, mainly for operations such as addition, subtraction, ....
# '''
# a = np.array([1, 2, 3], float)
# b = np.array([5, 2, 6], float)
# print("a+b", a + b)
# print("a-b", a - b)
# print("a*b", a * b)
# print("a/b", a / b)
# print("a%b", a % b)
# print("b**a", b ** a)
#
# ''' For multi-dimensional arrays, multiplication remains elementwise, and doesnot correspond to matrix multiplication. '''
# a = np.array([[1, 2], [3, 4]], float)
# b = np.array([[2, 0], [1, 3]], float)
#
# print("a,b", a, b)
# print("a*b = ", a * b)
#
# try:
#     print("Errors are thrown if arrays do not match in size.")
#     a = np.array([1, 2, 3], float)
#     b = np.array([4, 5], float)
#     print("a+b", a + b)
# except:
#     print("dimensions mismatch")
