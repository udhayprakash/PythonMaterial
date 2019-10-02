#!/usr/bin/python
"""
Purpose: Problem solving 

A = 1
B = 2*A + A = 3
C = 3*B + B = 12
D = 4*C + C = 60
.
.
.
Y = 25*X + X
Z =  26*Y + Y


weight = 20
          1 * 12 + 2 * 3 + 2 * 1
          1 *  C + 2 * B + 2 * A  = CBBAA = AABBCC

# assert smallest_string(20) == 'AABBC'
# assert smallest_string(46) == 'ABBBCCC'

HINT: dict, reverse_dict, ord(), chr()

"""
from pprint import pprint


def smallest_string(weight):
    values = {'A': 1}
    for index, i in enumerate(range(66, 65 + 26), start=3):
        values[chr(i)] = index * values[chr(i - 1)]

    # pprint(values)
    reverse_values = {v: k for k, v in values.items()}
    # pprint(reverse_values)

    # weight = 20 
    # assert 20 == 12 + 3 + 3 + 1 + 1

    result = ''
    for ech_num in tuple(reverse_values)[::-1]:
        quotient, remainder = divmod(weight, ech_num)
        if quotient:
            result += reverse_values[ech_num] * quotient
            weight = remainder

    return ''.join(sorted(result))


# print(smallest_string(4))
assert smallest_string(20) == 'AABBC'
assert smallest_string(4) == 'AB'
assert smallest_string(46) == 'ABBBCCC'

for i in range(100):
    print(i, smallest_string(i))
