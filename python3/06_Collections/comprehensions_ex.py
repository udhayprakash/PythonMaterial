new_list = []
for i in range(2, 9):
    new_list.append(i)

print(new_list)

# List comprehension
print([i for i in range(2, 9)])

##########
new_list = []
for i in range(2, 9):
    if i % 2 != 0:
        new_list.append(i)
print(new_list)

print([i for i in range(2, 9) if i % 2 != 0])
###################
new_list = []
for i in range(2, 9):
    if i % 2 != 0:
        new_list.append('odd')
    else:
        new_list.append('even')
print(new_list)

# Duck-typing

# Ternary operation
print('odd' if True else 'even')
print('correct' if 23 % 2 == 0 else 'not correct')
print(1 if 6 % 2 == 0 else 0)

print([i % 2 != 0 for i in range(2, 9)])
print(['odd' if i % 2 != 0 else 'even' for i in range(2, 9)])
# #########################################

my_variable = [ch for ch in 'Mangalyan']
print(type(my_variable), my_variable)

my_variable = (ch for ch in 'Mangalyan')
print(type(my_variable), my_variable)

my_variable = {ch for ch in 'Mangalyan'}
print(type(my_variable), my_variable)

my_variable = {ch: ord(ch) for ch in 'Mangalyan'}
print(type(my_variable), my_variable)

# chr(), ord()
print('chr(77) ', chr(77))
print("ord('M')", ord('M'))
# caesar cipher
# a b c d e f ......
# 0 1 2 3 4 5 .......
# +3
# bad -> edg
# ex: attack is planned to happen on next sunday

# HINT : % operation, chr(), ord()