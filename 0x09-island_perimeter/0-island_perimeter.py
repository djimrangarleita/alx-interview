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
                if i - 1 < 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if j - 1 < 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if i + 1 >= len(grid) or grid[i + 1][j] == 0:
                    perimeter += 1
                if j + 1 >= len(grid[i]) or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
