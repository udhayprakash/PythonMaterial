# for (int a = 0; a < 10 ; a ++)


# for loop can be applied on iterable object 
# (string, list, tuple, set, frozenset, dictionary, iterator, generator) only

language = "python programming"

# iterating over a string  
for i in language:
    print(i, end=' ')        
print()

# enumerate - gives the loop index
# iterating over a string
for loop_count, ch in enumerate(language):
    # print(loop_count, ch)
    # print("character at %d position is %s"%(loop_count, ch))
    print("character at %2d position is %1s" % (loop_count, ch))
# print()

numbers = [12, 34, 5, 6, 7, 99, 888]

# Iterating over a list of elements
for number in numbers:
    print(number, end=' ')
print()

for loop_count, number in enumerate(numbers):
    print(loop_count, '-->', number)

print('-'*20)
######################
data = list(range(-100,1000000, 3)) 
data_length = len(data)
for index, number in enumerate(data): 
    # print( '\r{} of {} completed'.format(index,data_length), end = '')
    print( '\r{0:.2f} completed'.format((100 *index)/data_length), end = '')
