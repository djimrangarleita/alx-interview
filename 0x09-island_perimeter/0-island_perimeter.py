#!/usr/bin/python3
"""Module to solve the island perimeter pb
"""


def island_perimeter(grid):
    """Island perimeter, iterative approach"""
    perimeter = 0
    if not grid:
        return 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                cell_perimeter = abs(grid[i - 1][j] - 1)\
                        + abs(grid[i][j - 1] - 1)\
                        + abs(grid[i + 1][j] - 1)\
                        + abs(grid[i][j + 1] - 1)
                perimeter += cell_perimeter
    return perimeter
