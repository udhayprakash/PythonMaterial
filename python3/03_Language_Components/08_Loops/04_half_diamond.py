#!/usr/bin/python
"""
Purpose: To display the astrickes in a half-diamond pattern
"""
# i = 0
# while i < 10:
#     print('*' * i)
#     i += 1

# # print(f'i:{i}')
# # i = 10
# while i > 0:
#     print('*' * i)
#     i -= 1


# print('-' * 20)

# for i in range(10):
#     print('*' * i)

# for i in range(10, 0, -1):
#     print('*' * i)

print('-' * 20)

for i in range(10):
    print( ' ' * (10-i) + '*' * i)

for i in range(10, 0, -1):
    print( ' ' * (10-i) + '*' * i)

print('-' * 20)


i = 0
while i < 10:
    print( ' ' * (10-i) + '*' * i)
    i += 1

while i > 0:
    print( ' ' * (10-i) + '*' * i)
    i -= 1

# assignent:full diamond problem
