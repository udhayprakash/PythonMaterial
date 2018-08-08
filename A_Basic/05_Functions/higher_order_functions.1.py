# zip, map, filter, reduce

group1 = ('1', '2', '3')
group2 = ('a', 'b', 'c', 'd')

print zip(group1, group2)
print dict(zip(group1, group2))
print

print map(None, group1, group2)
print dict(map(None, group1, group2))
