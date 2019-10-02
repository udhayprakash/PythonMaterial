#!/usr/bin/python
"""
Problem Statement:
	9
					1
				  2 1 2
				3 2 1 2 3
			  4 3 2 1 2 3 4
			5 4 3 2 1 2 3 4 5
		  6 5 4 3 2 1 2 3 4 5 6
		7 6 5 4 3 2 1 2 3 4 5 6 7
	  8 7 6 5 4 3 2 1 2 3 4 5 6 7 8
	9 8 7 6 5 4 3 2 1 2 3 4 5 6 7 8 9
	
"""

num = 6  # int(raw_input("n="))

max_width = len(" ".join(map(str, range(num, 0, -1))) + " ".join(map(str, range(2, num + 1)))) + 1
# max_width is the maximum width, i.e width of the last line

print("{0:^{1}}".format("1", max_width))  # print 1 , ^ is used to place the
# string in the center of the max_width
for i in range(2, num + 1):  # print rest of the numbers from 2 to num
    range1 = range(i, 0, -1)
    strs1 = " ".join(map(str, range1))
    range2 = range(2, i + 1)
    strs2 = " ".join(map(str, range2))
    print("{0:^{1}}".format(" ".join((strs1, strs2)), max_width))  # use ^ again with max_width
