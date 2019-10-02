#!/usr/bin/python
"""
Purpose: https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
"""

test_input = \
    '''
    29
    append 1
    append 6
    append 10
    append 8
    append 9
    append 2
    append 12
    append 7
    append 3
    append 5
    insert 8 66
    insert 1 30
    insert 6 75
    insert 4 44
    insert 9 67
    insert 2 44
    insert 9 21
    insert 8 87
    insert 1 75
    insert 1 48
    print
    reverse
    print
    sort
    print
    append 2
    append 5
    remove 2
    print'''


def execute_list_commands(test_input):
    my_list = []
    for ech_line in test_input.split('\n')[1:]:
        command = ech_line.split()
        if command[0] == 'print':
            print(my_list)
        elif command[0] == 'sort':
            my_list.sort()
        elif command[0] == 'reverse':
            my_list.reverse()  # sort(reverse=True)
        elif command[0] == 'pop':
            my_list.pop()
        elif command[0] == 'remove':
            my_list.remove(int(command[1]))
        elif command[0] == 'append':
            my_list.append(int(command[1]))
        elif command[0] == 'insert':
            my_list.insert(int(command[1]), int(command[2]))


execute_list_commands(test_input)

# [1, 48, 75, 30, 44, 6, 10, 44, 8, 9, 87, 75, 21, 2, 67, 12, 7, 66, 3, 5]
# [5, 3, 66, 7, 12, 67, 2, 21, 75, 87, 9, 8, 44, 10, 6, 44, 30, 75, 48, 1]
# [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87]
# [1, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87, 2, 5]
