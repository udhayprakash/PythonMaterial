#!/usr/bin/python
"""
Purpose: Towers of Hanoi Problem 
    Output a list of moves that solves the Towers of Hanoi.
        Input : An integer n.
        Output: A sequence of moves that solve the n-disk Towers of
                Hanoi puzzle.

"""


def hanoi_towers(n, from_peg, to_peg):
    if n == 1:
        print(f'Move disk from peg {from_peg} to peg {to_peg}')
        return

    unused_peg = 6 - from_peg - to_peg
    hanoi_towers(n - 1, from_peg, unused_peg)
    print(f'Move disk from peg {from_peg} to peg {to_peg}')
    hanoi_towers(n - 1, unused_peg, to_peg)
    return


hanoi_towers(4, 1, 3)
