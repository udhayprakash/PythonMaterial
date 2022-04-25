"""
Purpose: Using threaing.Lock()

    The acquire() method is used to lock access to a shared variable

    The release() method is used to unlock the lock.
    The release() method throws a RuntimeError exception if used on an unlocked lock.
"""
import threading


class Primenum(threading.Thread):
    prime_nums = {}
    lock = threading.Lock()

    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

        Primenum.lock.acquire()
        Primenum.prime_nums[num] = "None"
        Primenum.lock.release()

    def run(self):
        ctr = 2
        res = True
        while ctr * ctr < self.num and res:
            if self.num % ctr == 0:
                res = False
            ctr += 1

        Primenum.lock.acquire()
        Primenum.prime_nums[self.num] = res
        Primenum.lock.release()


threads = []
while True:
    input_val = int(input("number: "))
    if input_val < 1:
        print(f"{Primenum.prime_nums =}")
        break

    thread = Primenum(input_val)
    threads += [thread]
    thread.start()

for x in threads:
    x.join()
