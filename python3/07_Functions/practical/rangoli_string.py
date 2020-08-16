#!/usr/bin/python3

def print_rangoli(size):
    alphabets = [chr(i) for i in range(97, 97 + size)]
    rangoli_str_lst = []
    i = 1
    while i <= size:
        _chars = alphabets[-i:]
        rangoli_str_lst.append('-'.join(_chars[::-1] + _chars[1:]))
        i += 1

    window_size = len(rangoli_str_lst[-1])
    rangoli_str_lst = rangoli_str_lst[:-1] + rangoli_str_lst[::-1]

    for each in rangoli_str_lst:
        print(each.center(window_size, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
