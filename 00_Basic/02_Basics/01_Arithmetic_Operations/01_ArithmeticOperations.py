#!/usr/bin/python

"""
Purpose: Demonstration of Arithmetic Operations
"""

# + - * / // %

num1 = 10       # int 
num2 = 200      # int 


print "num1=", num1
print 'num2=', num2

print '-----------------------------'
print "Arithmetic Operations"
print '-----------------------------'

print 'Addition'
print 'num1 + num2 = ', num1 + num2
print
print 'Subtraction'
print 'num1 - num2 = ', num1 - num2
print
print 'Multiplication'
print 'num1 * num2 = ', num1 * num2
print
print 'Division'
print 'num1 / num2 = ', num1 / num2


# integers - int, long, float
print 'type(num1)= ', type(num1)
print 'type(num2)= ', type(num2)

# int < long < float
# int + int  = int

# int + long = long
# int + float = float
# long + float = float


num3 = 3445678909876545678909876556789098765
# the max. integer that can be computed depends on the capability of the machine

print 'num3 = ', num3
print 'type(num3)= ', type(num3)

print 'num1 + num3= ', num1 + num3  # long


# going back to division

print '10/2= ', 10/2   # int/int = int 
print '10/5= ', 10/5   # int/int = int

print '10/3= ', 10/3   # int/int = int    # 3.333333
print '10/3.0= ', 10/3.0   # int/float = float    # 3.333333


# type conversions
# int()
# float()
# long()

print 'int(3.333333)=', int(3.333333)
print 'float(3) = ', float(3)

print 'float(3.333) = ', float(3.333)

print '10/float(3)= ', 10/float(3)

print 'num1 / num2 = ', num1 / num2
print 'float(num1) / num2 = ', float(num1) / num2


print 'floor division  //'
print '10/3 = ', 10/3
print '10//3 = ', 10//3

print '10/3.0 = ', 10/3.0
print '10//3.0 = ', 10//3.0   # 3 < 3.3333 < 4 


print '10/2.5 = ', 10/2.5
print '10//2.5 = ', 10//2.5   # 4.0


'''
>>> 13/2
6
>>> 13/2.0
6.5
>>> 13//2.0
6.0
>>> - 13//2.0
-7.0
>>> - 13/2.0  # true result
-6.5
>>> # -7 < -6.5 < -6
'''


print 'Modulo Operation  % - remainder'

print '13 % 2=', 13 % 2

print '-13 % 2=', -13 % 2
print '13 % -2=', 13 % -2
print '-13 % -2=', -13 % -2

print 'power operation **'

print '4 ** 2 = ', 4 ** 2
print '64 ** 0.5 = ', 64 ** 0.5  # square root
print '64 ** (1/2) = ', 64 ** (1/2)

print 'pow(4,2)=', pow(4,2)
print 'pow(64,0.5)=', pow(64, 0.5)
print 'pow(64,1/2)=', pow(64,1/2)

print 'pow(4,2, 9)=', pow(4,2, 9)


print 'Exponent Notation'
print '1e1 = ', 1e1

print '1 * 10.0 ** 1 = ', 1 * 10.0 ** 1

print '3e2 =', 3e2   # 3 * 10.0 ** 2
print '-2.3e4 = ', -2.3e4
