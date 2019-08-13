def toString(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toString(n / base, base) + convertString[n % base]


print(toString(1453, 16))
print(toString(1453, 8))


#  mutually recursive functions 

def func1(num1):
    return func2(num1)

def func2(num2):
    return func1(num2)