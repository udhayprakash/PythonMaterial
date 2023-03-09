"""
Purpose: Solving this problem
    conventionally without using threads
"""
import time


def PrintSquare(numbers):
    print("Print squares of the given numbers")
    for n in numbers:
        time.sleep(0.2)
        print("Square", n * n)


def PrintCube(numbers):
    print("Print cubes of the given numbers")
    for n in numbers:
        time.sleep(0.2)
        print("Cube", n * n * n)


arr = [2, 3, 4, 5]

start = time.time()
PrintSquare(arr)
PrintCube(arr)

print("Program took", time.time() - start)
