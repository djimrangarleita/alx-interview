#!/usr/bin/python3
"""Module to solve the island perimeter pb
"""


def island_perimeter(grid):
    """Island perimeter, iterative approach"""
    perimeter = 0
    if not grid:
        return 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 0:
                perimeter += 4
                if i > 0 and grid[i - 1][j] != 0:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] != 0:
                    perimeter -= 2
    return perimeter
