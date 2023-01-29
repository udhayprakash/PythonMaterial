import time
from concurrent.futures import Future, ThreadPoolExecutor


def test():
    print("testing this")
    time.sleep(2)
    return "got"


sample = ThreadPoolExecutor(max_workers=2, thread_name_prefix="sample")

for _ in range(10):
    got: Future = sample.submit(test)
    print(
        got.result(timeout=3)
    )  # waits for the result (like the join)  # raise TimeoutError  (doesn't quit thread tho)
    # 2 threads at a time
    # plus those 2 threads are reused instead of creating new thread every time
    # that's how it's diff. from threading module

sample.shutdown(cancel_futures=True)
# refer: https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.shutdow
