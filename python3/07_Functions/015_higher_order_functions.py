# zip, map, filter, reduce
# function which were designed to work on another functions 
# are called higher-order functions 

group1 = ('1', '2', '3')
group2 = ('a', 'b', 'c', 'd')

print(list(zip(group2, group1)))
print(list(zip(group1, group2)))
print(dict(list(zip(group1, group2))))

print(dict([['1', 'a'], ['2', 'b'], ['3', 'c']]))
print()

# print(map(None, group1, group2))
# print(dict(map(None, group1, group2)))

print(list(map(my_mapper, group1, group2)))
print(dict(list(map(my_mapper, group1, group2))))

print(list(map(lambda x, y: {x:y}, group1, group2)))
print(dict(list(map(lambda x, y: {x:y}, group1, group2))))

print('-'* 25)

def check_positive(num):
    if num>= 0:
        return True 
    return False

print('check_positive ----')
#### Traditionally
result = []
for each_num in range(-4,6):
    result.append(check_positive(each_num))
print(result)

###### using map()
print(list(map(check_positive, range(-4, 6))))

#### Traditionally
result = []
for each_num in range(-4,6):
    if check_positive(each_num):
        result.append(each_num)
print(result)

#### using filter
print(list(filter(check_positive, range(-4, 6))))

print('----using comprehensions=========')
print([each_num>=0 for each_num in range(-4,6)])  # map
print([each_num for each_num in range(-4,6) if each_num>=0])  # filter

def double(x):
        return 2 * x

print('-----using lambda================== anonymous function')
print(list(map(double, range(-4, 6))))
print([2+x for x in range(-4, 6)])
print([num>=0 for num in range(-4, 6)])
print([num for num in range(-4, 6) if num>=0])
print()
print([x for x in range(9)])
print([x%2==0 for x in range(9)])
print([x for x in range(9) if x%2==0])
print()
print([x%2!=0 for x in range(9)])
print([x for x in range(9) if x%2!=0])
