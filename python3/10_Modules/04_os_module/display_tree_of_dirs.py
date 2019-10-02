#!/usr/bin/python
"""
Purpose: To display the tree strcuture of directories only , till three levels

test
   sub1
   sub2
       subsub1

"""
import os

MAX_DEPTH = 3  # levels 

given_path = r'C:\Python27\etc'  # input('Enter the path:')
print(given_path)


def display_folders(_path, _depth):
    if _depth != MAX_DEPTH:
        _depth += 1
        files_n_flders = os.listdir(_path)
        for each in files_n_flders:
            if os.path.isdir(os.path.join(_path, each)):
                print('  ' * _depth, each)
                display_folders(os.path.join(_path, each), _depth)


display_folders(given_path, 0)
