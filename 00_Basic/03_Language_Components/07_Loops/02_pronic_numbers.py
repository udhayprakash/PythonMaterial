#!python -u 
"""
Purpose: Display the pronic numbers.
 PRONIC NUMBER: Pronic number is a number which is the product
 of two consecutive integers.
 Some pronic numbers: 2*3 = 6

"""
 
n = int(raw_input("Enter a number: "))
 
for i in range(1, n):
    print i, i * (i+1) == n
    if i * (i+1) == n:
        print "%d is a pronic number." % n
        break
else:
    print 'All iterations in for loop completed'

print 'next statement'