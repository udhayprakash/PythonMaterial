"""
In commandline, 
    #python -m timeit "'-'.join(str(n) for n in range(10))"
    20000 loops, best of 5: 12.2 usec per loop

    #python -m timeit "'-'.join([str(n) for n in range(10)])"
    20000 loops, best of 5: 10.1 usec per loop

    #python -m timeit "'-'.join(map(str, range(10)))"
    20000 loops, best of 5: 9.05 usec per loop

SYNTAX:
python -m timeit [-n N] [-r N] [-u U] [-s S] [-h] [statement ...]

-n , --number  : how many times to execute ‘statement’
-r , --repeat  : how many times to repeat the timer (default 5)
-s , --setup   : statement to be executed once initially (default pass)
-u , --unit    : specify a time unit for timer output; can select nsec, usec, msec, or sec


#python -m timeit -n 20 "'-'.join(map(str, range(10)))"
20 loops, best of 5: 8.78 usec per loop

#python -m timeit -n 20 -r 15 "'-'.join(map(str, range(10)))"
20 loops, best of 15: 8.88 usec per loop

#python -m timeit -n 20 -r 15 -u msec "'-'.join(map(str, range(10)))"
20 loops, best of 15: 0.00783 msec per loop

#python -m timeit -n 20 -r 15 -u sec "'-'.join(map(str, range(10)))"
20 loops, best of 15: 7.8e-06 sec per loop

#python -m timeit -n 20 -r 15 -u sec -v "'-'.join(map(str, range(10)))"
raw times: 0.00035 sec, 0.000332 sec, 0.000336 sec, 0.000336 sec, 0.000335
sec, 0.000335 sec, 0.000654 sec, 0.000178 sec, 0.000176 sec, 0.000177 sec,
0.000176 sec, 0.000176 sec, 0.000176 sec, 0.000175 sec, 0.000176 sec

20 loops, best of 15: 8.75e-06 sec per loop
"""
import timeit
print(timeit.timeit('"-".join(str(n) for n in range(10))', number=10000))
print(timeit.timeit('"-".join([str(n) for n in range(10)])', number=10000))
print(timeit.timeit('"-".join(map(str, range(10)))', number=10000))

print(timeit.timeit(lambda: "-".join(map(str, range(10))), number=10000))

# By default, timeit() temporarily turns off garbage 
# collection during the timing.
print(timeit.Timer('for i in range(10): oct(i)', 'gc.enable()').timeit())


print('\n-----with setup')
"""
with setup,
    #python -m timeit -s "lang = 'Python'; char = 't'"  "char in lang"
    1000000 loops, best of 5: 141 nsec per loop

    #python -m timeit -s "lang = 'Python'; char = 't'"  "lang.find(char)"
    500000 loops, best of 5: 626 nsec per loop

"""
print(timeit.timeit("char in lang", setup="lang = 'Python'; char = 't'"))
# 0.15269916100000014
print(timeit.timeit("lang.find(char)", setup="lang = 'Python'; char = 't'"))
# 0.4405657889999999

# The same can be done alternatively,
print('\n-----with setup, alternatively')
t = timeit.Timer("char in lang", setup="lang = 'Python'; char = 't'")
print(t.timeit())
print(t.repeat())


print('\n----when test code has multiple lines')
"""
#python -m timeit "try:" "  str.__bool__" "except AttributeError:" "  pass"
100000 loops, best of 5: 2.01 usec per loop

#python -m timeit "if hasattr(str, '__bool__'): pass"
200000 loops, best of 5: 1.38 usec per loop

#python -m timeit "try:" "  int.__bool__" "except AttributeError:" "  pass"
1000000 loops, best of 5: 200 nsec per loop

#python -m timeit "if hasattr(int, '__bool__'): pass"
1000000 loops, best of 5: 256 nsec per loop
"""
# attribute is missing
s = """\
try:
    str.__bool__
except AttributeError:
    pass
"""
print(timeit.timeit(stmt=s, number=100000))

s = "if hasattr(str, '__bool__'): pass"
print(timeit.timeit(stmt=s, number=100000))


# attribute is present
s = """\
try:
    int.__bool__
except AttributeError:
    pass
"""
print(timeit.timeit(stmt=s, number=100000))

s = "if hasattr(int, '__bool__'): pass"
print(timeit.timeit(stmt=s, number=100000))


print('\n-----passing globals to use global variables')
def f(x):
    return x**2
def g(x):
    return x**4
def h(x):
    return x**8

# print(timeit.timeit('[func(42) for func in (f,g,h)]'))
# NameError: name 'f' is not defined
print(timeit.timeit('[func(42) for func in (f,g,h)]', globals=globals()))


# from timeit import timeit


# print(timeit("factorial(999)", "from math import factorial", number=10))


# from math import factorial
# print(timeit(lambda: factorial(999), number=10))