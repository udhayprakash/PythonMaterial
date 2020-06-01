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
num = int(input("Enter a number: ")) 

for i in range(1, num):
    # print(f'{i:2} * {i+1:2} = {i * (i + 1): 3}')

    if i * (i +1) == num:
        print(f'{num} is a PRONIC number')
        break
else:
    # print('All iterations in for loop completed')
    print(f'{num} is NOT PRONIC number')

# print('Next Statement')
