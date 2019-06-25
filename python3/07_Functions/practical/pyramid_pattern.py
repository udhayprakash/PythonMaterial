#!/usr/bin/python


"""
Problem statement: 
		
Enter number of lines 3
  *            prints 3-1=2 spaces, i=1 '* ' 
 * * 		   prints 3-2=1 space, i =2 '* '
* * * 		   prints 3-3=0 spaces, i =3 '* '
"""

n = int(eval(input('Enter number of lines ')))

for i in range(1, n + 1):
    print(((n -i) * ' ' + i * '* '))


def triangle(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print()  # observe the difference after importing print_function
            k = k - 1
    for j in range(0, i + 1):
        print("* ")
    print("\r")


n = 5
triangle(n)
