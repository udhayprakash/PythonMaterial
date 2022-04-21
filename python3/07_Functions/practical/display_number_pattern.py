#!/usr/bin/python
"""
Purpose: For input of two numbers(say (3,2)), to display number as below:

 07  09  11
   03  05
     01
     01
   03  05
 07  09  11

"""


def get_count(m):
    if m == 1:
        return 1
    return m + get_count(m - 1)


def series(_count):
    numbers = [1]
    while len(numbers) < _count:
        numbers.append(numbers[-1] + 2)
    return numbers


if __name__ == "__main__":
    upSeries, downSeries = 9, 8
    maxValue = max(upSeries, downSeries)  # 9
    count = get_count(maxValue)  # 9 + 8 +.. + 1 = 45
    numbersList = series(count)  # 45 odd numbers
    numberSeries = []
    for i in range(1, maxValue + 1):
        numberSeries.append(numbersList[:i])
        del numbersList[:i]

    print("FINAL OUTPUT")
    maxLen = upSeries  # len(numberSeries[::-1][:upSeries][0])
    for indx, num in enumerate(numberSeries[::-1]):  # numberSeries[::-1][:upSeries])
        print("  " * indx, "  ".join([str(i).zfill(2) for i in num]))

    for num in numberSeries[: downSeries + 1]:
        print("  " * indx, "  ".join([str(i).zfill(2) for i in num]))
        indx -= 1
