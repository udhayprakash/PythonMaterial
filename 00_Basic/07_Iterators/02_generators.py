def count(n):
    print "Stating to count!"
    i = 0
    while i<n:
        yield i
        # print i
        i+=1
    print '$', i
    # return i 

# PEP8 strongly discourages usage of yield and retun, in same function


c = count(9)
print c

print 'c.next() ', c.next()

print 'looping'
for val in c:
    print val