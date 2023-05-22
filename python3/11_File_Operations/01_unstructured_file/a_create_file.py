#!/usr/bin/python
"""
Purpose:
    file operations
        - read  - r
        - write - w -> if file not present, file will be created;
                       if present, existing content will be overwritten
        - append- a

        default is read mode

"""
# open('a_first_file.txt')
# FileNotFoundError: [Errno 2] No such file or directory: 'a_first_file.txt'

# open('a_first_file.txt', mode='r')
# # FileNotFoundError: [Errno 2] No such file or directory: 'a_first_file.txt'

# open('a_first_file.txt', mode='w')

file_handler = open("a_first_file.txt", mode="w")
print(f"{type(file_handler) =}")
print(f"{file_handler       =}")
# <_io.TextIOWrapper name='a_first_file.txt' mode='w' encoding='cp1252'>
print()

file_handler = open("a_first_file.txt", mode="w", encoding="utf-8")
print(f"{file_handler       =}")
# <_io.TextIOWrapper name='a_first_file.txt' mode='w' encoding='utf-8'>
print()

# To add content to file
file_handler.write("This is the first line\n")
file_handler.write("This is the second line\n")

file_handler.close()
