#!/usr/bin/python
"""
How to print nested array ? 
Input : [1, 5, 8, [9, 10, 24, 20, [39, 48], 89], 105, 99] 
Output : 1, 5, 8, 9, 10, 24, 20, 39, 48, 89, 105, 99. 

Which data structure you will use to store the values?
"""


def display_nested_array(given_input):
    for each_ele in given_input:
        if type(each_ele) == type([]):
            display_nested_array(each_ele)
        else:
            print(each_ele)


input_list = [1, 5, 8, [9, 10, 24, 20, [39, 48], 89], 105, 99]
display_nested_array(input_list)
