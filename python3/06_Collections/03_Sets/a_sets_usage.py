#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Purpose: Working with Sets
    Properties of sets
        - creating using {} or set()
        - can't store duplicates
        - sets are unordered
        - can't be indexed
        - Empty sets need to be represented using set()
        - stores only immutable object - basic types, tuple, string
        - sets are mutable objects
"""
running_ports = [11, 22, 11, 44, 22, 11]
print("type(running_ports)", type(running_ports))
print("len(running_ports) ", len(running_ports))
print("running_ports      ", running_ports)
print()

# Method 1 - To remove duplicates in a list/tuple of elements
filtered_list = []
for each_port in running_ports:
    if each_port in filtered_list:
        continue
    filtered_list.append(each_port)

print("len(filtered_list) ", len(filtered_list))
print("filtered_list:     ", filtered_list)

print()
unique_ports = {11, 22, 11, 44, 22, 11}
print(f"{type(unique_ports) =}")
print(f"{len(unique_ports)  =}")
print(f"{unique_ports       =}")
print()


# Method 2 - using sets to remove duplicates
filtered_list = list(set(running_ports))
print("len(filtered_list) ", len(filtered_list))
print("filtered_list:     ", filtered_list)
print()
