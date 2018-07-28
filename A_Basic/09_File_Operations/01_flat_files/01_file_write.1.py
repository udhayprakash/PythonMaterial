with open('myfile.txt', 'ab') as f:
    f.write('\ndate is 26th July 2018')
    f.close()


with open('myfile.txt', 'rb') as g:
    data = g.read()
    print 'data\n', data
    g.close()