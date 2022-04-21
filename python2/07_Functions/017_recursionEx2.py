def toString(n, base):
    convertString = '0123456789ABCDEF'
    if n < base:
        return convertString[n]
    else:
        return toString(n / base, base) + convertString[n % base]


print toString(1453, 16)
print toString(1453, 8)
