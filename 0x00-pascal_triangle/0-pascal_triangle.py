#!/usr/bin/python3
"""Pascal triangle problem
"""


def pascal_triangle(n):
    """Pascal triangle solution with t: O(n^2)"""
    if (n <= 0):
        return []
    result = [[1]]
    for i in range(n - 1):
        tmp = [0] + result[-1] + [0]
        row = []
        for j in range(len(tmp) - 1):
            row.append(tmp[j] + tmp[j + 1])
        result.append(row)
    return result
