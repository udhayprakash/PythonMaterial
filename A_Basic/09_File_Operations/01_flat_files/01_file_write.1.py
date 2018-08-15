
# files -- read , write , append
       #   r       w      a
       #   rb      wb     ab

with open('myfile.txt', 'wb') as f:
    f.write('\ndate is 14th August 2018')
    f.close()


with open('myfile.txt', 'rb') as g:
    data = g.read()
    print 'data\n', data
    g.close()

##############

with open('myfile.txt', 'ab') as f:
    f.write('\ndate is 14th August 2018')
    f.close()


with open('myfile.txt', 'rb') as g:
    data = g.read()
    print 'data\n', data
    g.close()