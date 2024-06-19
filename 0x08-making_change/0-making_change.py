#!/usr/bin/python3

"""import typing, the type anotation module"""
from typing import List


def makeChange(coins, total):
    """functiom that determines the fewest number of
       coins needed to meet a given amount totat

        Args:
          coins: List[int] = is a list with coins used to get total.
          total: int = the number that coins should add up too.

        Return:
          - returns the length of the number of coins used
    """
    coins.sort(reverse=True)
    result: List[int] = []

    if total <= 0:
        return (0)

    for coin in coins:
        while total >= coin:
            result.append(coin)
            total -= coin

            if total == 0:
                break
    """ return -1 If total cannot be met by
        any number of coins you have
    """
    if total > 0:
        return (-1)

    return (len(result))
