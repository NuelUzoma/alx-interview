#!/usr/bin/python3
"""a function def island_perimeter(grid):
that returns the perimeter of the island described in grid"""


def solve(matrix):
    """The function of the program"""
    d = 0
    perimeter = 0
    height = len(matrix)
    length = len(matrix[0])
    for line in matrix:
        c = 0

        for val in line:
            if val == 1:
                surround = 4
                if c != length - 1:
                    if matrix[d][c + 1] == 1:
                        surround -= 1
                if c != 0:
                    if matrix[d][c - 1] == 1:
                        surround -= 1
                if d != height - 1:
                    if matrix[d + 1][c] == 1:
                        surround -= 1
                if d != 0:
                    if matrix[d - 1][c] == 1:
                        surround -= 1
                perimeter += surround
            c += 1
        d += 1
    return perimeter
