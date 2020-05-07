#!/usr/bin/python
"""
Purpose: Importance of context manager


Q) what is the interval at which the garbage collector will check for unreferenced objects
Ans) depends on the system clock cycle
        2.3 GHz
"""
# Method 1: traditional
fh = open('something.tsf', 'r')

data = fh.read()
print(data)

fh.close()
# fh.read()
# ValueError: I/O operation on closed file.



# Method 2: with context manager
with open('something.tsf', 'r') as fh:
    data = fh.read()

# fh.read()
# ValueError: I/O operation on closed file.

# ------------WRITE OPS---------------------
# Method 1: traditionally
gh = open('someTHing.txt', 'w')
# gh.writelines(['1', '2', '3', '4'])
gh.writelines(['1\n', '2\n', '3\n', '4\n'])
gh.flush()
gh.close()
# gh.write('next') # ValueError: I/O operation on closed file.


# Method 2: Using context manager
with open('someTHing.txt', 'w') as gh:
    gh.writelines(['1', '2', '3', '4'])

# gh.write('next') # ValueError: I/O operation on closed file.