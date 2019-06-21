with open('myfile.txt', 'a+') as g:
    print "cursor before reading --- g.tell()", g.tell()
    data = g.read(8)
    print(data)
    print(type(data))
    # print(dir(g))
    print "cursor after reading --- g.tell()", g.tell()

    some_more_data = g.readline()
    print 'some_more_data', some_more_data
    print "cursor after reading line--- g.tell()", g.tell()
    
    some_more_data1 = g.readline()
    print 'some_more_data1', some_more_data1
    print "cursor after reading line--- g.tell()", g.tell()

    print 
    print 'before closing ---g.closed', g.closed
    g.close()
    print 'after closing  ---g.closed', g.closed
    