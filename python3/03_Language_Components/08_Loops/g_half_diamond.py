#!/usr/bin/python
"""
Purpose: To display the asterisk's in a half-diamond pattern
"""
__name__ = 'Author'

# half - diamond
for num in range(0, 10, 1):
    print(num * '*')

for num in range(10, 0, -1):
    print(num * '*')

# half - diamond
for num in range(0, 10, 1):
    print((10 - num) * ' ' + num * '*')

for num in range(10, 0, -1):
    print((10 - num) * ' ' + num * '*')

# ---------------------------------------------
# half - diamond
i = 0
while i < 10:
    print(i * '*')
    i += 1

# print(i)  # 10
while i > 0:
    print(i * '*')
    i -= 1

# half - diamond
i = 0
while i < 10:
    print((10 -i) * ' ' + i * '*')
    i += 1

# i = 10
while i > 0:
    print((10 -i) * ' ' + i * '*')
    i -= 1

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
