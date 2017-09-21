#!/usr/bin/python
"""
Purpose:

There are two files: file1.txt and file2.txt

If there are any common files between file1.txt and file2.txt, they must be
removed from file2.txt
"""

with open('file1.txt', 'rb') as file1:
    file1_data = file1.readlines()
        # gives list of strings(each line is a string)
    file1.close()
    
with open('file2.txt', 'rb') as file2:
    file2_data = file2.readlines()
        # gives list of strings(each line is a string)
    file2.close()


# Method 1
#for lines1 in file1_data:
#    if lines1 in file2_data:
#        #print lines1
#        file2_data.remove(lines1)
#
# result = file2_data

# Method 2 
result = set(file2_data) - set(file1_data)  # set difference operation


# writing that data to file2_formatted.txt
with open('file2_formatted.txt', 'wb') as frmt_file:
    frmt_file.writelines(result)




