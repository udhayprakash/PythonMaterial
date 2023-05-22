#!/usr/bin/python
"""
Purpose: file write operations
    possible modes: w, w+
"""
new_fh = open("e_write_multiple_lines.upp", mode="w", encoding="utf-8")

# To write a single line
new_fh.write("first line 1111111\n")

remaining_lines = ("second\n", "third\n", "fourth\n", "fifth\n", "sixth\n")
# # Method 1 - To write multiple lines
# for each_line in remaining_lines:
#     new_fh.write(each_line)

# Method 2 - To write multiple lines
new_fh.writelines(remaining_lines)  # it accepts iteratable of strings

new_fh.flush()
new_fh.close()
