#!/usr/bin/python3
"""
Purpose: To display the asterisk's in a half-diamond pattern
"""
# half-diamond
for num in range(0, 10, 1):
    print(num * '*')

for num in range(10, 0, -1):
    print(num * '*')

for num in range(0, 10, 1):
    print((10 - num) * ' ' + num * '*')

for num in range(10, 0, -1):
    print((10 - num) * ' ' + num * '*')

# half-diamond using while
i = 0
while i < 10:
    i += 1
    print(i * '*')

# i = 10
while i > 0:
    i -= 1
    print(i * '*')

i = 0
while i < 10:
    i += 1
    print((10 - i) * ' ' + i * '*')

# i = 10
while i > 0:
    i -= 1
    print((10 - i) * ' ' + i * '*')

'''
Assignment:full diamond problem
       *
      ***
     *****
    *******
   *********
  ***********
 *************
***************
 *************
  ***********
    *******
     *****
      ***
       *
'''
for num in range(0, 10, 1):
    print((10 - num) * ' ' +  (2 * num  - 1) * '*')

for num in range(10, 0, -1):
    print((10 - num) * ' ' +  (2 * num  - 1) * '*')
