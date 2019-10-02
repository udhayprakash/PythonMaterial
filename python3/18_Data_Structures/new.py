#!/usr/bin/python
"""
Purpose: Problem Solving 
given an array A of N integers, returns the smallest 
positive integer (greater than 0) that does not occur 
in A.
"""


def solution(A):
    result = sorted(set(filter(lambda x: x > 0, A)))
    if (not result) or (result[0] != 1):
        return 1
    for index, ech_num in enumerate(result):
        try:
            if result[index + 1] - ech_num > 1:
                return ech_num + 1
        except IndexError:
            pass
    return result[-1] + 1


assert solution([3, 2, -1]) == 1
assert solution([-1, -3]) == 1
assert solution([1, 3, 6, 4, 1, 2]) == 5
assert solution([1, 2, 3]) == 4
assert solution([1, 3, 3]) == 2
assert solution([0, 0, 0]) == 1
assert solution([1, 1, 1]) == 2
assert solution([-1, -1, -1]) == 1
assert solution([-5, -4, -5, -6, 0, -1, -2]) == 1
assert solution([-1, -7, 7, 2, 1]) == 3
assert solution([-1, -7, 7, 2, 1, -6]) == 3
