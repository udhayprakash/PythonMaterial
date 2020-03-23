# def toString(n, base):
#     convertString = "0123456789ABCDEF"
#     if n < base:
#         return convertString[n]
#     else:
#         return toString(n / base, base) + convertString[n % base]
#
#
# print(toString(1453, 16))
# print(toString(1453, 8))


# -----------------------
import sys

print(f'sys.getrecursionlimit():{sys.getrecursionlimit()}')
sys.setrecursionlimit(2000)
print(f'sys.getrecursionlimit():{sys.getrecursionlimit()}')

#  mutually recursive functions
count = [0]


def func1(num1):
    count[0] += 1
    print(f'loop:{count[0]}')
    return func1(num1)

func1(9)

def func1(num1):
    count[0] += 1
    print(f'loop:{count[0]}')
    return func2(num1)


def func2(num2):
    return func1(num2)


func1(9)
