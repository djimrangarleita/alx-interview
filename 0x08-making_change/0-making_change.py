#!/usr/bin/python3
"""Module to solve the coin change problem
"""


def makeChange(coins, total):
    """Return the minimum num of coins used to make total"""
    if total <= 0:
        return 0
    result = [total + 1] * (total + 1)
    result[0] = 0
    for i in range(total + 1):
        for coin in coins:
            if coin > i:
                continue
            result[i] = min(result[i], 1 + result[i - coin])
            if coin == i:
                break
    if result[total] > total:
        return -1
    return result[total]
