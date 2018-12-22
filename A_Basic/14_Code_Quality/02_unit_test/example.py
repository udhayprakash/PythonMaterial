# ch6_example.py

def first(chars):
    chars.sort()
    return chars[0]


def last(chars):
    chars.sort()
    return chars[-1]


if __name__ == '__main__':
    list_nums = [7, 9, 5]
    print last(list_nums)
