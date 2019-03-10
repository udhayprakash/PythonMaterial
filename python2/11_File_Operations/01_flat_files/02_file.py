with open('myfile.txt') as f:
    data = f.read()
    print 'data:\n', data
    f.close()

# default mode is "read only"