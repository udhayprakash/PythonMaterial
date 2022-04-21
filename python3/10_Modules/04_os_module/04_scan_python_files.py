#!/usr/bin/python3
"""
Purpose: Script to get
    all the files in a directory and its sub-directories,
    of a particular extension
"""
import os


# function definition
def get_files_of_particular_extn(extension_name, path_file=os.getcwd()):
    """
    To get the files of a particular extension within the directory and subdirectories
    :param extension_name: extension name such as .py, .png, .jpg, ...
    :param path_file: relative or absolute directory path
    :return: list of matched files
    """
    extn_files = []
    for present_path, folders, files in os.walk(path_file):
        # print(present_path,folders, files)
        for each_file in files:
            file_extn = os.path.splitext(each_file)[1]
            # print(file_extn)
            if file_extn == extension_name:
                # print(each_file)
                extn_files.append(each_file)
        # break
    return extn_files


if __name__ == '__main__':
    # function call
    extension_specific_files = get_files_of_particular_extn('.py')
    print('extension_specific_files:')
    for file_name in extension_specific_files:
        print(file_name)

    print('total files count', len(extension_specific_files))
    print('os.getcwd():', os.getcwd())
    print('-' * 20)

    custom_path = 'C:\Users\udhayPrakash\Desktop\PythonMaterial\A_Basic'
    extension_specific_files = get_files_of_particular_extn('.py', custom_path)
    print('extension_specific_files:')
    for file_name in extension_specific_files:
        print(file_name)

    print('total files count', len(extension_specific_files))
else:
    print('imported')
