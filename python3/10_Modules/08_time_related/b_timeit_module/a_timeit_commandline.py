"""
In commandline,
    ~python -m timeit "'-'.join(str(n) for n in range(10))"
    100000 loops, best of 5: 2.48 usec per loop

    ~python -m timeit "'-'.join(str(n) for n in range(10))"
    100000 loops, best of 5: 2.94 usec per loop

    ~python -m timeit "'-'.join(map(str, range(10)))"
    200000 loops, best of 5: 2.23 usec per loop

SYNTAX:
python -m timeit [-n N] [-r N] [-u U] [-s S] [-h] [statement ...]

-n , --number  : how many times to execute ‘statement’
-r , --repeat  : how many times to repeat the timer (default 5)
-s , --setup   : statement to be executed once initially (default pass)
-u , --unit    : specify a time unit for timer output; can select nsec, usec, msec, or sec

~python -m timeit -n 20 "'-'.join(map(str, range(10)))"
20 loops, best of 5: 2.72 usec per loop
:0: UserWarning: The test results are likely unreliable. The worst time (12.2 usec) was more than four times slower than the best time (2.72 usec).

~python -m timeit -n 20 "'-'.join(map(str, range(10)))"
20 loops, best of 5: 2.43 usec per loop

~python -m timeit -n 20 -r 15 "'-'.join(map(str, range(10)))"
20 loops, best of 15: 1.75 usec per loop

~python -m timeit -n 20 -r 15 -u msec "'-'.join(map(str, range(10)))"
20 loops, best of 15: 0.00168 msec per loop

~python -m timeit -n 20 -r 15 -u sec "'-'.join(map(str, range(10)))"
20 loops, best of 15: 1.72e-06 sec per loop

~python -m timeit -n 20 -r 15 -u sec -v "'-'.join(map(str, range(10)))"
raw times: 6.91e-05 sec, 6.67e-05 sec, 6.58e-05 sec, 6.78e-05 sec, 9.45e-05 sec, 5.89e-05 sec, 6.74e-05 sec, 6.73e-05 sec, 6.66e-05 sec, 6.13e-05 sec, 6.02e-05 sec, 0.000449
sec, 7.09e-05 sec, 8.62e-05 sec, 5.8e-05 sec

20 loops, best of 15: 2.9e-06 sec per loop
:0: UserWarning: The test results are likely unreliable. The worst time (2.24e-05 sec)
was more than four times slower than the best time (2.9e-06 sec).

~python -m timeit -n 20 -r 15 -u sec -v "'-'.join(map(str, range(10)))"
raw times: 3.9e-05 sec, 3.49e-05 sec, 3.46e-05 sec, 3.46e-05 sec, 3.55e-05 sec, 3.47e-05 sec, 3.46e-05 sec, 3.47e-05 sec, 3.45e-05 sec, 3.47e-05 sec, 3.46e-05 sec, 3.47e-05 sec, 3.46e-05 sec, 3.47e-05 sec, 3.44e-05 sec

20 loops, best of 15: 1.72e-06 sec per loop

~python -m timeit -n 20 -r 5 -u usec -v "'-'.join(map(str, range(10)))"
raw times: 38.7 usec, 40.4 usec, 50.5 usec, 34.6 usec, 34.5 usec

20 loops, best of 5: 1.72 usec per loop
"""
