# for (int a = 0; a < 10 ; a ++)

# for loop can be applied on iterable object 
# (string, list, tuple, set, frozenset, dictionary, iterator, generator) only

language = "python programming"

# iterating over a string  
for i in language:
    print(i, end=' ')        
print()

# for i in 12312:  # TypeError: 'int' object is not iterable
    # print(i)

for i in '12312':
    print(i)


for index, ch in enumerate(language):
    # print(index, ch)
    # print('In loop %2d, we got %s'%(index, ch))
    # print('In loop {:2}, we got {}'.format(index, ch))
    print(f'In loop {index:2}, we got {ch}')



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

data = list(range(-100,10_00_000, 3)) 
data_length = len(data)

for index, number in enumerate(data): 
    # print('%f' % (index/data_length) * 100)
    val = round((index/data_length) *100, 2)
    # print('\r', val, end='')
    print(f'\r {val:5} % completed', end='')


# # Assignment 
# # Progress bar implementation