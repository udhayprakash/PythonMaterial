#!/usr/bin/python

class RationalNumber:
    """
    Rational Numbers with support for arthmetic operations.

        >>> a = RationalNumber(1, 2)
        >>> b = RationalNumber(1, 3)
        >>> a + b
        5/6
        >>> a - b
        1/6
        >>> a * b
        1/6
        >>> a/b
        3/2
    """
    def __init__(self, numerator, denominator=1):
        self.n = numerator
        self.d = denominator

    def __add__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n = self.n * other.d + self.d * other.n
        d = self.d * other.d
        return RationalNumber(n, d)


    def __str__(self):
        return "%s/%s" % (self.n, self.d)

    __repr__ = __str__
    
# Main
a = RationalNumber(1,2)  # a.n = 1,a.d=2
b = RationalNumber(2,3)
c = 29
print isinstance(a,RationalNumber)
print isinstance(b,RationalNumber)
print isinstance(c,RationalNumber)
print a + b

