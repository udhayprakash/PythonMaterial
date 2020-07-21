import os

PATH = 'C:\Python27\Tools'

for dir_path, dir_name, filename in os.walk('PATH'):
    print(dir_path, dir_name, filename)
