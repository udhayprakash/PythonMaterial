# !/usr/bin/python
__author__ = 'udhay Prakash'


# 1, 2, 3, 4, 5
def stringreverse(string):
    print(string)
    if string == '':
        return ''
    else:
        # print(string[1:])
        # print(string[0])
        return stringreverse(string[1:]) + string[0]


'''
1st loop
    stringreverse(string[1:]) + string[0]
                  "23456"        "1"
    stringreverse(string[1:]) + string[0]
                  "3456"         "2"
    stringreverse(string[1:]) + string[0]
                  "456"        "3"
    stringreverse(string[1:]) + string[0]
                  "56"         "4"
    stringreverse(string[1:]) + string[0]
                  "6"        "5"
    stringreverse(string[1:]) + string[0]
                  ""         "6"

    ""+"6"+ "5" + "4"+ "3"+ "2"+ "1"
'''
print(stringreverse('123456'))

"""
Recursion:
1. logic for computation
2. condition to end the loop
"""
flag = True

while flag:
    if 1:
        flag = False
    elif 2:
        flag = False
    else:
        pass
