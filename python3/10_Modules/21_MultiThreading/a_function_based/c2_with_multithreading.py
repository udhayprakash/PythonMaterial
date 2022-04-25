# This multithreading program prints output
# of square and cube of a series of numbers


import threading
import time


def PrintSquare(numbers):
    print("Print squares")
    for n in numbers:
        time.sleep(0.2)
        print("Square", n * n)


def PrintCube(numbers):
    print("Print cubes")
    for n in numbers:
        time.sleep(0.2)
        print("Cube", n * n * n)


arr = [2, 3, 4, 5]
t = time.time()

PrintSquare(arr)
PrintCube(arr)

t1 = threading.Thread(target=PrintSquare, args=(arr,))
t2 = threading.Thread(target=PrintCube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Program took", time.time() - t)
