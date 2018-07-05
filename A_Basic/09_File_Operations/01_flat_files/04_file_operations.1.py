with open('myfile.txt', 'ab+') as g:
    print "cursor before reading --- g.tell()", g.tell()
    data = g.read()
    print data
    print type(data)
    # print dir(g)
    print "cursor after reading --- g.tell()", g.tell()


    print 'before closing ---g.closed', g.closed
    g.close()
    print 'after closing  ---g.closed', g.closed
    