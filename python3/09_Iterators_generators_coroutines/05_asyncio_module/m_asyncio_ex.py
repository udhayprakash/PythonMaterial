import os
import sys
import concurrent.futures

THREAD_POOL = concurrent.futures.ThreadPoolExecutor(max_workers=5)


def slow_op(*args):
    python_license = os.path.join(sys.exec_prefix, 'LICENSE.txt')
    with open(python_license, 'rb') as f:
        return f.read(50)


def do_something():
    future = THREAD_POOL.submit(slow_op, 'a', 'b', 'c')

    THREAD_POOL.shutdown()

    assert future.done() and not future.cancelled()

    print(f'got the result from slow_op: {len(future.result())}')


if __name__ == '__main__':
    print('program started')
    do_something()
    print('program complete')
