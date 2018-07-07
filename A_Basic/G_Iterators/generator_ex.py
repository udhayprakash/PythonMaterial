def func(n):
    for i in range(n):
        print i


def func1(n):
    for i in range(n):
        return i



def func2(n):
    for i in range(n):
        yield i


print "func(5) ", func(5)
print "func1(5) ", func1(5)
print "func2(5) ", func2(5)

f5 = func2(5)

print f5

print f5.next()
print 5* f5.next()
print f5.next()
print f5.next()
print f5.next()
#print 'finally', f5.next()

for i in f5:
    print i
