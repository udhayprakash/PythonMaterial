# fibonacci Generator
# 0, 1, 1, 2, 3, 5, 8, ...
def fib(num):
    a,b = 0,1
    if num < 0:
        yield "ivalid input"
    elif num == 0:
        yield a 
    for i in range(0, num):
        yield "{}:{}".format(i+1, a)
        a,b = b, a+b

for item in fib(-1):
    print(item)
