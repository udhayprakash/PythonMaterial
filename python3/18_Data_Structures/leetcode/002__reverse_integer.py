#!/usr/bin/python
"""
Purpose: 
    https://leetcode.com/problems/reverse-integer/

"""


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            val = -1 * int(str(-1 * x)[::-1].lstrip('0'))
        elif x == 0:
            val = 0
        else:
            val = int(str(x)[::-1].lstrip('0'))

        return val if pow(-2, 31) < val < pow(2, 31) - 1 else 0


s = Solution()
assert s.reverse(123) == 321
assert s.reverse(-123) == -321
assert s.reverse(120) == 21
assert s.reverse(1534236469) == 0
