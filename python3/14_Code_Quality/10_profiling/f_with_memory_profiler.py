"""
Purpose: Profiling with memory profiler

    pip install memory_profiler psutil

"""
from memory_profiler import profile


# @profile
def func1():
    mylist1 = []
    for i in range(10_000):
        mylist1.append(i)


@profile
def memory_intensive():
    small_list = [None] * 1000000
    big_list = [None] * 10000000
    del big_list
    return small_list


@profile
def my_func():
    a = [1] * (10**6)
    b = [2] * (2 * 10**7)
    del b
    return a


@profile(precision=4)
def my_func2():
    a = [1] * (10**6)
    b = [2] * (2 * 10**7)
    del b
    return a


if __name__ == "__main__":
    func1()
    memory_intensive()
    my_func()
    my_func2()
