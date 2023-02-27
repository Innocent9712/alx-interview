#!/usr/bin/python3
"""0. Island Perimeter"""


def island_perimeter(grid):
    """a function that returns the perimeter
    of the island described in grid
    """
    if len(grid) == 0:
        return 0
    parameter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                parameter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    parameter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    parameter -= 2
    return parameter
