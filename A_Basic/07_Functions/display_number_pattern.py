#!/usr/bin/python
"""
Purpose: For input of two numbers(say (3,2)), to display number as below:

 07  09  11
   03  05
     01
     01
   03  05

"""


def getCount(m):
    if m == 1:
        return 1
    return m + getCount(m - 1)


def series(count):
    numbers = [1]
    while len(numbers) < count:
        numbers.append(numbers[-1] + 2)
    return numbers


if __name__ == '__main__':
    upSeries, downSeries = 3, 2
    maxValue = max(upSeries, downSeries)
    # print "maxValue:", maxValue
    count = getCount(maxValue)
    # print "count:", count
    numbersList = series(count)
    # print "numbersList:", numbersList
    numberSeries = []
    for i in range(1, maxValue + 1):
        numberSeries.append(numbersList[:i])
        del numbersList[:i]

    # print "numberSeries:", numberSeries

    print "FINAL OUTPUT"
    maxLen = len(numberSeries[::-1][:upSeries][0])
    for indx, num in enumerate(numberSeries[::-1][:upSeries]):
        print '  ' * indx, '  '.join([str(i).zfill(2) for i in num])

    for num in numberSeries[:downSeries]:
        print '  ' * indx, '  '.join([str(i).zfill(2) for i in num])
        indx -= 1
