#!/usr/bin/python
"""
Purpose: Progress Bar
"""
data = list(range(-100, 1000000, 3))
data_length = len(data)
# for index, number in enumerate(data):
#     # print( '\r{} of {} completed'.format(index,data_length), end = '')
#     print( '\r{0:.3f} completed'.format((100 *index)/data_length), end = '')

values = {0: "|", 1: "/", 2: "-", 3: "\\"}
for index, _ in enumerate(data):
    print("\r", values.get(index % 4), "Loading ...", end=" ")
