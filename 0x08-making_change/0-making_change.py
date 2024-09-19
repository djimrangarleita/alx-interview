#!/usr/bin/python3
"""Coin change problem"""


def makeChange(coins, total):
    """Return the min num of coins used to make total"""
    if total <= 0:
        return 0
    if not coins:
        return -1
    result = [float('inf')] * (total + 1)
    result[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            result[i] = min(result[i], result[i - coin] + 1)
    if result[total] != float('inf'):
        return result[total]
    return -1
