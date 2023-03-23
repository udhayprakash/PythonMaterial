"""
Purpose: This program adds two given numbers and
prints the result.
"""

import threading


def addition(num1, num2):
    """This is user defined thread function"""
    print("Given numbers= %s, %s" % (num1, num2))
    print("Result = %d" % (int(num1) + int(num2)))


def Main():
    t = threading.Thread(target=addition, args=(12, 13))
    t.start()


if __name__ == "__main__":
    Main()
