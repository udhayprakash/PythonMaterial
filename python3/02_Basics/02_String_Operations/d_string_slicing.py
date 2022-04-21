#!/usr/bin/python3
"""
Purpose: String slicing operations
"""
print('String Slicing')  # [start_index: final_index]

# P   y  t  h  o n     P r o g  r  a  m  m  i  n  g
# 0   1  2  3  4 5 6   7 8 9 10 11 12 13 14 15 16 17   - forward indexing
# -18                                      -3 -2 -1    - reverse indexing
language = 'Python Programming'
print('language       :', language)
print('language[0]    :', language[0])

print()
print('language[0:11] :', language[0:11])
print('language[5:17] :', language[5:17])
print('language[7:10] :', language[7:10])

# NOTE: In python, it doesn't include the last value,
# in a boundary condition.
print()
print('language[0:5]  :', language[0:5])
print('language[0:6]  :', language[0:6])

print()
print('language[7:18] :', language[7:18])
print('language[7:999]:', language[7:999])  # 999 index isn't present
print('language[45:87]:', language[45:87])  # indexes are not present

# string slicing :-
#   string[start_index: final_index: step]
#   Default Step is +1
print()
print('language[7:18]   =', language[7:18])
print('language[7:18:1] =', language[7:18:1])
# [7:18:1] => 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17


# P   y  t  h  o n   P r o g  r  a  m  m  i  n  g
# 0   1  2  3  4 5 6 7 8 9 10 11 12 13 14 15 16 17    - forward indexing
# -18                                    -3 -2 -1    - reverse indexing
print()
print('language[7:18:3] =', language[7:18:3])
# [7:18:3] => 7, 10, 13, 16


print('language[7:18:-1]=', language[7:18:-1])
# 7-1 = 6 ; it is not between 7 and 18
# [7:18:-1]  =>

print('language[17:7:-1]', language[17:7:-1])  # 17-1 = 16
# [17:7:-1]  => 17, 16, 15, 14, 13, 12, 11, 10, 9, 8

print('language[17:6:-1]', language[17:6:-1])  # 17-1 = 16
# [17:6:-1]  =>17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7


# -> slicing above the limit
print('language[18:6:-1]', language[18:6:-1])  # 18-1 = 17
# [18:6:-1]  => 18, 17, 16, 15, ......8, 7
#  -1           17, 16, 15, 14, ......7

print('language[18:7:-3]', language[18:7:-3])  # 18-3 = 15
# [18:7:-3] => 18, 15, 12, 9
#  -1          17, 14, 11, 8

# P   y  t  h  o n   P r o g  r  a  m  m  i  n  g
# 0   1  2  3  4 5 6 7 8 9 10 11 12 13 14 15 16 17    - forward indexing
# -18                                    -3 -2 -1    - reverse indexing

print('language[23:7:-3]', language[23:7:-3])  # 23 -3 = 20
# [23:7:-3] => 23, 20, 17, 14, 11, 8
#  -6          17, 14, 11,  8
#               g  m    r   r


print('language[25:7:-2]', language[25:7:-2])  # 25 -2 = 23
# [25:7:-2] => 25, 23, 21, 19, 17, 15, 13, 11, 9
#  -8          17, 15, 13, 11, 9
#               g  i   m   r   o
