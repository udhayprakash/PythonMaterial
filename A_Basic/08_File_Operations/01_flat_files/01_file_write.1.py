from __future__ import print_function
# files -- read , write , append
       #   r       w      a
       #   rb      wb     ab
       #   r+      w+       a+

# default mode is 'read'
my_file_handler = open('myfile.txt')
print(my_file_handler)
print(dir(my_file_handler))

print("my_file_handler.closed", my_file_handler.closed)
print("my_file_handler.read()", my_file_handler.read())
# .read -- all content as single string
# .readline ---  current line as a string
# .readlines --- all content as a list of strings, each string containing one line data
my_file_handler.close()
print("my_file_handler.closed", my_file_handler.closed)
# print("my_file_handler.read()", my_file_handler.read())#ValueError: I/O operation on closed file


with open('myfile.txt') as g: #, 'rb'
    data = g.read()
    g.close()

print('data\n', data)

with open('myfile.txt', 'wb') as f:
    f.write('\ndate is 14th August 2018')
    f.close()



# f.read --- str ing 
# f.readline --- string
# f.readlines() -- list of strings



##############

with open('myfile.txt', 'ab') as f:
    f.write('\ndate is 14th August 2018')
    f.close()


with open('myfile.txt', 'rb') as g:
    data = g.read()
    print('data\n', data)
    g.close()