with open('myfile.txt', 'a+') as g:
    # import pdb; pdb.set_trace()
    # breakpoint()
    print("cursor before reading --- g.tell()", g.tell())
    data = g.read()
    print("data:\n", data)
    print(type(data))
    # print dir(g)
    print("cursor after reading --- g.tell()", g.tell())
    data = g.read()
    print("data", data)

    # to change the position of the cursor
    g.seek(60)
    print('after g.seek(60)-------- g.tell()', g.tell())
    data = g.read()
    print("data", data)

    g.seek(-3, 2)  # Go to the 3rd byte before the end

    print('before closing ---g.closed', g.closed)
    g.close()
    print('after closing  ---g.closed', g.closed)
