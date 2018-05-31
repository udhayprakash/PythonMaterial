def count(n):
    print "Stating to count!"
    i = 0
    while i<n:
        yield i
        i+=1
    print '$', i
    # return i 

# PEP8 strongly discourages usage of yield and retun, in same function


c = count(9)
print c

for val in c:
    print val