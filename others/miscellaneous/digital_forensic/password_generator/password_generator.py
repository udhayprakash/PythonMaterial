#!/usr/bin/env python
"""
This program generates passwords based on three arguments passed:
* seed - which can be any string, eg. website domain
* salt - salt, which together with seed provides X and Y position for
char matrix
* length - which is simply the length of generated password

Sample usage:
./password_generator.py facebook salt123 40

Output:
hz8s=tdmSD<\wdBmSqivGBZ42KX3LZokvS?TXoh

which is pretty strong password, don't you think? :)
"""
import sys

from matrix import matrix


def get_char_from_matrix(x, y):
    """Returns char from matrix from position [x][y]"""
    return matrix[x][y]


def update_position(length, pos):
    """Increments actual cursor position in salt or seed"""
    return 0 if pos + 1 == length else pos + 1


def generate():
    """Generates password from seed and salt"""
    generated = ""

    # pass_length of seed:
    seed_length = len(seed)
    seed_pos = 0

    # pass_length of salt:
    salt_length = len(salt)
    salt_pos = 0

    for i in range(0, int(pass_length) - 1):
        x = ord(seed[seed_pos]) - 1
        y = ord(salt[salt_pos]) - 1
        generated += get_char_from_matrix(x, y)

        seed_pos = update_position(seed_length, seed_pos)
        salt_pos = update_position(salt_length, salt_pos)

    return generated


if __name__ == "__main__":
    # get seed, salt and password pass_length from ARGS
    seed = sys.argv[1]
    salt = sys.argv[2]
    pass_length = sys.argv[3]

    generated_password = generate()
    print generated_password
