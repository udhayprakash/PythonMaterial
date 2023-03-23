import threading


class PrimeNumber(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        ctr = 2
        while ctr * ctr < self.num:
            if self.num % ctr != 0:
                print(f"{ctr} * {self.num / ctr} ={self.num} - Not prime")
                return
            ctr += 1
        print(f"{self.num} is a prime number")


threads = []
while True:
    input_val = int(input("number: "))
    if input_val < 1:
        break

    thread = PrimeNumber(input_val)
    threads += [thread]
    thread.start()

for x in threads:
    x.join()
