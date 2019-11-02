#!/usr/bin/python
"""
Purpose: To display the astrickes in a half-diamond pattern
"""
###################################
for num in range(10):
    print(' ' * (10 -num) + '*' * num)

for num in range(10, 0, -1):
    print(' ' * (10 -num) + '*' * num)

###################################
for num in range(10):
    print('*' * num + ' ' * (10 -num))

for num in range(10, 0, -1):
    print('*' * num + ' ' * (10 -num) )

###################################

i = 0
while i < 10:
    print(' ' * (10 -i) + '*' * i)
    i += 1

j = 10
while j > 0:
    print(' ' * (10 -j) + '*' * j)
    j -= 1


i = 0
while i < 10:
    print('*' * i + ' ' * (10 -i) )
    i += 1

j = 10
while j > 0:
    print('*' * j + ' ' * (10 -j))
    j -= 1


'''
assignent:full diamond problem
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
