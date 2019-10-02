#!/usr/bin/python

def half_triangle_pattern(n):
    """
    *
    * *
    * * *
    * * * *
    * * * * *
    """
    for i in range(1, n + 1):
        print('* ' * i)


def half_triangle_numbers(n):
    """
    1
    2 2
    3 3 3
    4 4 4 4
    5 5 5 5 5
    """
    for i in range(1, n + 1):
        print(f'{i} ' * i)


def half_triangle_numbers_2(n):
    """
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    """
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()


def half_triangle_alphabets(n):
    """
    A
    B B
    C C C
    D D D D
    E E E E E
    """
    for i in range(65, 65 + n):
        print(f'{chr(i)} ' * (i - 65 + 1))


def half_triangle_alphabets_2(n):
    """
    A
    A B
    A B C
    A B C D
    A B C D E
    """
    for i in range(1, n + 1):
        for j in range(65, 65 + i):
            print(chr(j), end=' ')
        print()


"""
        1
     1  1  1
  1  1  1  1  1
1 1  1  1  1  1  1
  1  1  1  1  1  
     1  1  1 
        1
"""
if __name__ == '__main__':
    half_triangle_pattern(5)
    print('-' * 10)
    half_triangle_numbers(5)
    print('-' * 10)
    half_triangle_numbers_2(5)
    print('-' * 10)
    half_triangle_alphabets(5)
    print('-' * 10)
    half_triangle_alphabets_2(5)
