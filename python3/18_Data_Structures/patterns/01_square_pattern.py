#!/usr/bin/python

def square_pattern(n):
    """
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *
    """
    for i in range(n):
        print('* ' * n)


def square_number_pattern(n):
    """
    1 1 1 1 1
    2 2 2 2 2
    3 3 3 3 3
    4 4 4 4 4
    5 5 5 5 5
    """
    for i in range(1, n + 1):
        print(f'{i} ' * n)


def square_number_pattern_2(n):
    """
    1 2 3 4 5
    1 2 3 4 5
    1 2 3 4 5
    1 2 3 4 5
    1 2 3 4 5
    """
    for _ in range(1, n + 1):
        for i in range(1, n + 1):
            print(i, end=' ')
        print()


def square_alphabets_pattern(n):
    """
    A A A A A
    B B B B B
    C C C C C
    D D D D D
    E E E E E
    """
    for i in range(65, 65 + n):
        print((chr(i) + ' ') * n)


def square_alphabets_pattern_2(n):
    """
    A B C D E
    A B C D E
    A B C D E
    A B C D E
    A B C D E
    """
    for _ in range(n):
        for i in range(65, 65 + n):
            print(chr(i), end=' ')
        print()


def square_numbers_reverse(n):
    """
    5 5 5 5 5
    4 4 4 4 4
    3 3 3 3 3
    2 2 2 2 2
    1 1 1 1 1
    """
    for i in range(n, 0, -1):
        print('%s ' % (i) * n)


def square_numbers_reverse_2(n):
    """
    5 5 5 5 5
    4 4 4 4 4
    3 3 3 3 3
    2 2 2 2 2
    1 1 1 1 1
    """
    for _ in range(n):
        for i in range(n, 0, -1):
            print(i, end=' ')
        print()


def square_numbers_descending(n):
    """
    5 5 5 5 5
    4 4 4 4 4
    3 3 3 3 3
    2 2 2 2 2
    1 1 1 1 1
    """
    for i in range(n, 0, -1):
        print(f'{i} ' * n)


def square_numbers_descending_2(n):
    """
    5 4 3 2 1
    5 4 3 2 1
    5 4 3 2 1
    5 4 3 2 1
    5 4 3 2 1
    """
    for _ in range(n):
        for i in range(n, 0, -1):
            print(i, end=' ')
        print()


def square_alphabets_descending(n):
    """
    E E E E E
    D D D D D
    C C C C C
    B B B B B
    A A A A A
    """
    for i in range(n - 1, -1, -1):
        print(f'{chr(i + 65)} ' * n)


def square_alphabets_descending_2(n):
    """
    E D C B A
    E D C B A
    E D C B A
    E D C B A
    E D C B A
    """
    for _ in range(n):
        for i in range(n - 1, -1, -1):
            print(chr(i + 65), end=' ')
        print()


def custom_pattern_1(n):
    """
       0 0 0 0 0 0 0
       0 1 1 1 1 1 0
       0 1 1 1 1 1 0
       0 0 0 0 0 0 0
    """
    pass


if __name__ == '__main__':
    print('-' * 10)
    square_pattern(5)
    print('-' * 10)
    square_number_pattern(5)
    print('-' * 10)
    square_number_pattern_2(5)
    print('-' * 10)
    square_alphabets_pattern(5)
    print('-' * 10)
    square_alphabets_pattern_2(5)
    print('-' * 10)
    square_numbers_reverse(5)
    print('-' * 10)
    square_numbers_reverse_2(5)
    print('-' * 10)
    square_numbers_descending(5)
    print('-' * 10)
    square_numbers_descending_2(5)
    print('-' * 10)
    square_alphabets_descending(5)
    print('-' * 10)
    square_alphabets_descending_2(5)
    print('-' * 10)
