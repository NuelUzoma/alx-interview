#!/usr/bin/python3
"""
Create a function that returns a list of lists of integers
representing the Pascal's Triangle of `n`
"""


def pascal_triangle(n):
    """The required function to run the program"""
    if (n <= 0):
        return []
    triangle = [[1]]

    for i in range(1, n):
        row = [1] + [0] * (i - 1) + [1]

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
