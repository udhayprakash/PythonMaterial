with open('myfile.txt', 'a+') as g:
    print "cursor before reading --- g.tell()", g.tell()
    data = g.readlines()
    print(data)
    print(type(data))
    print(dir(g))
    print("cursor after reading --- g.tell()", g.tell())
    print('-----read again')
    some_more_data = g.read()
    print('some_more_data', some_more_data)
    print("cursor after reading --- g.tell()", g.tell())

    # to change the cursor position 
    g.seek(9)
    print('cursor position after g.seek(9)', g.tell())
    print('-----read again after cursor position change')
    current_line_content = g.readline()
    print('current_line_content', current_line_content)
    some_more_data1 = g.read()
    print('some_more_data1', some_more_data1)
    print("cursor after reading --- g.tell()", g.tell())

    print
    print('before closing ---g.closed', g.closed)
    g.close()
    print('after closing  ---g.closed', g.closed)
    