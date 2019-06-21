# Method 1
f = open('myfile.txt', 'w')
f.write('something')
f.flush()
f.close()



# Method 2 -context manager
with open('myfile.txt', 'w') as f:
    f.write('line 222222\n')
    f.write('line 333333\n')
    # my_data = ('ONE', 'TWO', 'THREE')
    # f.writelines(my_data)
    f.close()

# Q) what is the interval at which the garbage collector will check for unreferenced objects 
# Ans) depends on the system cock cycle 
#         2.3 GHz

# Assignment
# Take a list of strings, and try to place in file.
# HINT: f.writelines()
