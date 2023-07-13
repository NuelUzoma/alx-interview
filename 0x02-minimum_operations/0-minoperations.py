#!/usr/bin/python3
"""The required documentation for this task has been documentated
in the README.md of the directory"""


def minOperations(n):
    """The function for the program"""
    if n <= 1:
        return 0
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n /= i
        else:
            i += 1

    if not factors:
        return 0

    return sum(factors)
