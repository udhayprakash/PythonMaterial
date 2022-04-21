with open('myfile.txt', 'rb') as f:
    data = f.read()
    print 'data:\n', data
    f.close()
