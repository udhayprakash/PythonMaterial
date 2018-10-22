with open('myfile.txt', 'ab+') as g:
    print "cursor before reading --- g.tell()", g.tell()
    data = g.read()
    print("data", data)
    print type(data)
    # print dir(g)
    print "cursor after reading --- g.tell()", g.tell()
    data = g.read()
    print("data", data)

    # to change the position of the cursor
    g.seek(60)
    print('after g.seek(60)-------- g.tell()', g.tell())
    data = g.read()
    print("data", data)
    print 'before closing ---g.closed', g.closed
    g.close()
    print 'after closing  ---g.closed', g.closed
    