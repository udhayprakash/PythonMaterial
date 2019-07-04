# zip, map, filter, reduce
# function which were designed to work on another functions 
# are called higher-order functions 

group1 = ('1', '2', '3')
group2 = ('a', 'b', 'c', 'd')

print(zip(group2, group1))
print(list(zip(group2, group1)))
print(list(zip(group1, group2)))
print(dict(zip(group1, group2)))

print(dict([['1', 'a'], ['2', 'b'], ['3', 'c']]))
print()


print(list(
        zip(
                (1, 2, 3, 4),
                (11, 22, 33, 44),
                (111, 222, 333, 444),
        )
))

print(map(None, group1, group2))
print(dict(map(None, group1, group2)))

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
print(check_positive(-0))
#### Traditionally
result = []
for each_num in range(-4,6):
    result.append(check_positive(each_num))
print(result)

##### using map()
print(list(map(check_positive, range(-4, 6))))

#### Traditionally
result = []
for each_num in range(-4,6):
    if check_positive(each_num):
        result.append(each_num)
print(result)

#### using filter
print(list(map(check_positive,    range(-4, 6))))
print(list(filter(check_positive, range(-4, 6))))

print('----using comprehensions=========')
print([each_num for each_num in range(-4,6)])  
print([each_num>=0 for each_num in range(-4,6)])  # map
print([each_num for each_num in range(-4,6) if each_num>=0])  # filter

def double(x):
        return 2 * x

print('-----using lambda================== anonymous function')
print([2*x for x in range(-4, 6)])
print(list(map(double, range(-4, 6))))
print(list(map(lambda x:x*2, range(-4, 6))))

print([num*2 for num in range(-4, 6) if num])
print(list(map(double, range(-4, 6))))
print(list(filter(double, range(-4, 6))))
print(list(filter(lambda x:x*2>=3, range(-4, 6))))

# display all the even numbers between -5 & 17
print([each_num for each_num in range(-5, 17) if each_num%2==0])
print(list(map(lambda p:p%2==0, range(-5, 17))))
print(list(filter(lambda p:p%2==0, range(-5, 17))))
