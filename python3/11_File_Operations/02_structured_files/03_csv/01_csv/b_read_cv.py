"""
Purpose: Reading(Parsing) csv, using unstructure file ops
"""
# Method 1
with open("my_file.csv", mode="r") as fh:
    file_content = fh.read()


# print(file_content.split())
# print(file_content.splitlines())

names = []
for each_line in file_content.splitlines()[1:]:
    name = each_line.split(',')[1]
    names.append(name)

print(f"{names = }")
# names = ['akhila Bhopal', 'neha', 'hiral']



# Method 2
with open("my_file.csv", mode="r") as fh:
    file_content = fh.readlines()

names = []
for each_line in file_content[1:]:
    name = each_line.split(',')[1]
    names.append(name)

print(f"{names = }")
