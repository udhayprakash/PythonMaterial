# zip, map, filter, reduce
# function which were designed to work on another functions 
# are called higher-order functions 

group1 = ('1', '2', '3')
group2 = ('a', 'b', 'c', 'd')

print zip(group1, group2)
print dict(zip(group1, group2))
print

print map(None, group1, group2)
print dict(map(None, group1, group2))

print '-'* 25

print map(lambda x:x, xrange(9))
print map(lambda x:x%2==0, xrange(9))
print filter(lambda x:x%2==0, xrange(9))
print
print map(lambda x:x%2!=0, xrange(9))
print filter(lambda x:x%2!=0, xrange(9))


def check_positive(num):
    if num>= 0:
        return True 
    else:
        return False

print 'check_positive ----'
print map(check_positive, xrange(-4, 6))
print filter(check_positive, xrange(-4, 6))


print '\n reduce functionality'

print reduce(lambda p,q: p +q, xrange(6)) 
      # xrange(6) - [0, 1, 2, 3, 4, 5]
print map(lambda p,q: p +q, xrange(6),  xrange(6))
