def foo():   # definition
    print "Start the function!"
    for i in range(3):
        print "before yield", i
        yield i
        print "after yield", i
    print "end of function "
    
f = foo()  # call 
print f.next()
print 
print f.next()
print 
print f.next()
print 
print f.next()