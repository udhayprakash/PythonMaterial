#!/usr/bin/python
"""
Purpose: Dictionaries
    - This is representation of the data strcuture 
        - HashMap 
    - Properties 
        - reprsented using {} or dict()
"""

empty_dict = {}
print(empty_dict, type(empty_dict))

empty_dict = dict()
print(empty_dict, type(empty_dict))

empty_set = set()
print(empty_set, type(empty_set))

# - with values 
print()
other_set = {12, 34}
print(other_set, type(other_set))

other_dict = {12: 34, 34: 56}
print(other_dict, type(other_dict))

dict_with_single_pair = {'a': 1}
print(dict_with_single_pair, type(dict_with_single_pair))
