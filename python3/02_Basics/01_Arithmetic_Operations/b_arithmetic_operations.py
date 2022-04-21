#!/usr/bin/python3
"""
Purpose: Arithmetic Operations

    NOTE: PEP 8 recommends to place one space around the operator

"""
print('power operation **')
print('4 ** 2           = ', 4 ** 2)
print('64 ** (1/2)      = ', 64 ** (1 / 2))  # square root
print('64 ** (1/2.0)    = ', 64 ** (1 / 2.0))  # square root
print('64 ** 0.5        = ', 64 ** 0.5)  # square root
print()

# Operator precedence - PEMDAS
print('64 ** 1/2        = ', 64 ** 1 / 2)  # 32
print('(64 ** 1)/2      = ', (64 ** 1) / 2)# 32
print('64 ** (1/2)      = ', 64 ** (1 / 2))# 8.0
print()

print('pow(4,2)         =', pow(4, 2))
print('pow(64,1/2)      =', pow(64, 1 / 2))
print('pow(64,1/2.0)    =', pow(64, 1 / 2.0))
print('pow(64,0.5)      =', pow(64, 0.5))
print()

print('pow(4,2,9)       =', pow(4, 2, 9))  # (4 ** 2) % 9
print('(4**2) % 9       =', (4 ** 2) % 9)
print()

# == value level equivalence check - check LHS & RHS
print('pow(4, 2, 9) == (4 ** 2) % 9:', pow(4, 2, 9) == (4 ** 2) % 9)
print(pow(0, 0) == 0 ** 0 == 1)
print()

print('Exponent Notation/Representation')
print('1e1           = ', 1e1)
print('1 * 10.0 ** 1 = ', 1 * 10.0 ** 1)

print('3e2           =', 3e2)  # 3 * 10.0 ** 2
print('-2.3e4        = ', -2.3e4)  # -2.3 * 10.0 ** 4
print('velocity of light', 3e8)  # 3 * 10.0 ** 8
