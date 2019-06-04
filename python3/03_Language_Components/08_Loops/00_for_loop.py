# for (int a = 0; a < 10 ; a ++)


# for loop can be applied on iterable object 
# (string, list, tuple, set, frozenset, dictionary, iterator, generator) only

language = "python programming"

# iterating over a string  
for i in language:
    print(i, end=' ')        
print()


for index, ch in enumerate(language):
    # print(index, ch)
    print('In loop {:2}, we got {}'.format(index, ch))



numbers = [12, 34, 5, 6, 7, 99, 888]

# Iterating over a list of elements
for number in numbers:
    print(number, end=' ')
print()

for loop_count, number in enumerate(numbers):
    print(loop_count, '-->', number)

print('-'*20)
######################
print('udhay\tprakash')
print('udhay\nprakash')
print()
print('udhay\rprakash')
print('prakash\rudhay')

print('1234567890\rDOG')

data = list(range(-100,1000000, 3)) 
data_length = len(data)

for index, number in enumerate(data): 
    print('\r{:2}'.format(index/data_length), end='')


# Assignment 
# Progress bar implementation