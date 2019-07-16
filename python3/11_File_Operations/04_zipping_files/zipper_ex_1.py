#!/usr/bin/python
"""
Purpose: 
Take a backup zip file for all files on desktop
"""
import os 
from zipfile import ZipFile

# for each in os.environ:
#     print(each)

desktop_path = os.environ['USERPROFILE'] + os.sep + 'Desktop'
print(os.path.exists(desktop_path))

print(os.listdir(desktop_path))


with ZipFile('desktop.zip', 'w') as fh:
    for dir_pth, dirs, files in os.walk(desktop_path):
        for each_file in files:
            _file = os.path.join(dir_pth, each_file)
            print(_file)
            fh.write(_file)

    fh.close()
        




















# import os
# from datetime import datetime
# from zipfile import ZipFile


# def zipdir(path, zip):
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             zip.write(os.path.join(root, file))

# if __name__ == '__main__':
#     # set file name and time of creation
#     breakpoint()
#     today = datetime.now()
#     dir_name = os.environ.get('TEMP', None)  # update path
#     print('dir_name', dir_name)
#     file_name = dir_name + os.sep + 'zipper_' + today.strftime('%Y.%m.%d_h%H%M') + '.zip'
#     print('file_name', file_name)

#     # Zipping work
#     with ZipFile(file_name, 'w') as zipfile:
#         print(os.path.exists(file_name))
#         zipdir(dir_name, zipfile)
#         zipfile.close()
