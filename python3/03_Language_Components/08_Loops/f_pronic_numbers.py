#!python -u
"""
Purpose: Display the pronic numbers.

 Pronic number is a number which is the product
 of two consecutive integers.
 Some pronic numbers: 2*3 = 6

3  - 1 * 3
4  - 2 * 2
5  - 1 * 5
6  - 2 * 3  PRONIC
10 - 2 * 5

break
    - keyword
    - to stop the loop

NOTE:
else block of for loop will be executed, when all
iterations of for loop are completed
"""
# num = int(input('Enter a number:'))
# for i in range(1, num):
#     # print(i, i+1, i * (i+1))

#     if num == i * (i + 1):
#         print(f'{i:2} * {i+1:2} = {i * (i + 1): 3}')
#         print(f'{num} is a PRONIC number')
#         break
# else:
#     # print('All iterations in for loop completed')
#     print(f'{num} is NOT PRONIC number')

# print('Next Statement\n\n\n')


# # Get pronic numbers between 0 and 100
# for num in range(0, 100):
#     for i in range(1, num):
#         if num == i * (i + 1):
#             print(f'\t{i:2} * {i+1:2} = {i * (i + 1): 3}')
#             print(f'{num} is a PRONIC number')

# Get the first 100 pronic numbers
num = 0
pronic_nums_count = 0
while pronic_nums_count < 100:
    num += 1

    for i in range(1, num):
        if num == i * (i + 1):
            print(num, end = ',')
            pronic_nums_count += 1
