#!/usr/bin/python
"""
Purpose:

https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true

sample input: 10 30
sample Output:
10 30
-------------.|.--------------
----------.|..|..|.-----------
-------.|..|..|..|..|.--------
----.|..|..|..|..|..|..|.-----
-.|..|..|..|..|..|..|..|..|.--
-----------WELCOME------------
----.|..|..|..|..|..|..|.-----
-------.|..|..|..|..|.--------
----------.|..|..|.-----------
-------------.|.--------------
"""
n, m = map(int, input('Enter two values space separated, second value should be thrice of first\n').split())

if 5 < n < 101 and 15 < m < 303:
    for row in range(1, n):
        if row % 2 != 0:
            print(('.|.' * row).center(m, '-'))

    print('WELCOME'.center(m, '-'))

    for row in range(n - 2, 0, -1):
        if row % 2 != 0:
            print(('.|.' * row).center(m, '-'))
