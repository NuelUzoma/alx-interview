#!/usr/bin/python3
"""The Prime Game Task consisting of two users and a set of consecutive
integers from 1 up to n"""


def isWinner(x, nums):
    """The function of the program"""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = [True] * (n+1)
        primes[0] = primes[1] = False

        # Sieve of Eratosthenes to find all prime numbers up to n
        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n+1, p):
                    primes[i] = False
            p += 1

        # Determine the winner of the current round
        if sum(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
