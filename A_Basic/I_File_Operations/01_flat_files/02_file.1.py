with open('myfile.txt', 'rb') as f:
    data = f.read()
    print 'data', data
    f.close()