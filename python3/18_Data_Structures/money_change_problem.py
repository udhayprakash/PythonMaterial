#!/usr/bin/python
""""
Purpose: Money change problem 
Q) Convert some amount of money into given denominations, using the smallest
possible number of coins.

Input: An integer money and an array of d denominations c =(c1, c2, ....., cd),
       in decreasing order of value (c1 > c2 > ··· > cd).
Output: A list of d integers i1,i2,...,id such that c1 · i1 + c2 · i2 +
        ··· + cd · id = money; and i1 + i2 + ··· + id is as small as possible.

"""


def change(money, coins, denominations):
    r = money
    i = []
    # breakpoint()
    for k in range(denominations):
        i.append(r // coins[k])
        r = r - coins[k] * i[k]
    return i


money = 77
coins = (25, 10, 5, 1)
denominations = len(coins)

print(change(money, coins, denominations))  # [3, 0, 0, 2] = 3 * 25 + 1 * 2
