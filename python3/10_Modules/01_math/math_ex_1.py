import math

print(math.sqrt(2)/2.0)
print(1.0/math.sqrt(2.0))

print(math.sqrt(2)/2.0 == 1.0/math.sqrt(2.0))


print('math.sin(90)     ', math.sin(90))
degrees = 45
radians = degrees/360.0 * 2 * math.pi
print('math.pi          ', math.pi)
print('math.sin(radians)', math.sin(radians))

print('math.factorial(9)', math.factorial(9))

print(math.ceil(9.7))
print(math.ceil(9.5))
print(math.ceil(9.1))

print(int(9.7))
print(int(9.5))
print(int(9.1))

print()
print(abs(9))
print(abs(-9))

print()
print(math.fabs(9))
print(math.fabs(-9))

print(dir(math))
