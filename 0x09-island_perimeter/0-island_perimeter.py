#!/usr/bin/python3
"""A function def island_perimeter(grid): that returns the
perimeter of the island described in grid"""


def island_perimeter(grid):
    """The function to get the perimeter of the island"""
    rows = len(grid)
    columns = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:  # land cell
                perimeter += 4  # each land cell has four slides

                # adjacent cells check
                if i > 0 and grid[i-1][j] == 1:  # upper cell
                    perimeter -= 2  # subtract 2 sides (top and bottom)
                if j > 0 and grid[j-1][i] == 1:  # lower cell
                    perimeter -= 2  # subtract 2 sides (top and bottom)

    return perimeter
