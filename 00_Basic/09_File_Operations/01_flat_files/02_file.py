with open('myfile.txt') as f:
    data = f.read()
    print 'data', data
    f.close()

# default mode is "read only"