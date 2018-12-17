import doctest


def solution1(prices):
    """

    :param prices:
    :return:
    >>> solution1([2, 1, 2, 0, 1])
    2
    >>> solution1([7, 6, 4, 3, 1])
    0
    """
    sum1 = 0
    buy_index = 0

    while True:
        while (buy_index + 1 < len(prices) and
               prices[buy_index] > prices[buy_index + 1]):
            buy_index += 1

        sell_index = buy_index + 1

        while (sell_index + 1 < len(prices) and
               prices[sell_index] < prices[sell_index + 1]):
            sell_index += 1

        if (sell_index >= len(prices)
                or buy_index >= len(prices)):
            break

        sum1 += prices[sell_index] - prices[buy_index]
        buy_index = sell_index + 1

    return sum1


def solution2(prices):
    """
    :input: Given an integer array
    :return: Maximum profit
    >>> solution2([2, 1, 2, 0, 1])
    2
    >>> solution2([7, 6, 4, 3, 1])
    0
    """
    sum1 = 0
    buy_index = 0

    while True:
        while (buy_index + 1 < len(prices) and
               prices[buy_index] > prices[buy_index + 1]):
            buy_index += 1

        sell_index = buy_index + 1

        while (sell_index + 1 < len(prices) and
               prices[sell_index] < prices[sell_index + 1]):
            sell_index += 1

        if (sell_index >= len(prices) or
                buy_index >= len(prices)):
            break

        sum1 += prices[sell_index] - prices[buy_index]
        buy_index = sell_index + 1

    return sum1


if __name__ == '__main__':
    doctest.testmod()
