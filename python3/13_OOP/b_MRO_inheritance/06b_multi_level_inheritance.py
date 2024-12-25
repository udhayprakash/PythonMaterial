"""
Purpose: Multi-level inheritance

"""

class X:
    pass

class Y:
    pass

class Z:
    pass

class A(X,Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

if __name__ == '__main__':
    print(M.mro())

