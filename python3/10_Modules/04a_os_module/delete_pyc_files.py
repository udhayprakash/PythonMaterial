#!/usr/bin/python
"""
Purpose: Script to get all the files in a directory and its sub-directories , of a
particular extension
"""
import os


# function definition
def delete_pyc_files(path_file=os.getcwd()):
    """
    To get the files of a particular extension within the directory and subdirectories
    :param extension_name: extension name such as .py, .png, .jpg, ...
    :param path_file: relative or absolute directory path
    :return: list of matched files
    """
    extn_files = []
    for present_path, folders, files in os.walk(path_file):
        print(present_path, folders, files)
        for each_file in files:
            file_extn = os.path.splitext(each_file)[1]
            # print(file_extn)
            if file_extn == ".pyc":
                # print(present_path + os.sep + each_file)
                # delete those files
                os.remove(present_path + os.sep + each_file)
                extn_files.append(present_path + os.sep + each_file)
        # break
    return extn_files


if __name__ == "__main__":
    # function call
    custom_path = "D:/training/batch125"
    extension_specific_files = delete_pyc_files(custom_path)
    print("extension_specific_files:")
    for file_name in extension_specific_files:
        print("\t", file_name)

    print("total files deleted:", len(extension_specific_files))
else:
    print("imported")
