import collections
import concurrent.futures
import os
import time
from pprint import pprint


def transform(x):
    print("Process {} working record {}".format(os.getpid(), x.name))
    time.sleep(1)
    result = {"name": x.name, "age": 2019 - x.born}
    return result


Scientist = collections.namedtuple("Scientist", ["name", "field", "born", "nobel"])

scientists = (
    Scientist(name="Udhay", field="math", born=1947, nobel=True),
    Scientist(name="Prakash", field="science", born=1860, nobel=False),
    Scientist(name="Teja", field="physics", born=1770, nobel=True),
    Scientist(name="Ravi", field="math", born=1999, nobel=False),
    Scientist(name="Navya", field="physics", born=1947, nobel=False),
)

if __name__ == "__main__":
    pprint(scientists)
    print()

    start = time.time()

    # pool = multiprocessing.Pool() #(processes=2, maxtasksperchild=1)#(processes=len(scientists))
    # # default - it will process as much as capacity of CPU on system
    # result = pool.map(transform, scientists)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        result = executor.map(transform, scientists)
    end = time.time()

    print("\nTime to complete: {}".format(end - start))
    pprint(result)
    pprint(tuple(result))
