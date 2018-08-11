
# definition
def foo():  
    print "Start the function!"
    for i in range(3):
        print "before yield", i
        # return i
        yield i
        print "after yield", i
    print "end of function "
     


# call 
f = foo() 
print 'f', f 
print f.next()
print
print f.next()
print
print f.next()
print
# print f.next()  # StopIteration

try:
    print f.next()
except StopIteration:
    print 'error is StopIteration'

print 'using loop to get remaining elements'
for i in f:
    print i


print "====reinitialize call "
f = foo() 
for i in f:
    print i