#!/usr/bin/python3
"""Given a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total"""


def makeChange(coins, total):
    # Create a table to store the minimum number of coins
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through all the coins
    for coin in coins:
        # For each coin, update the table values
        for i in range(coin, total + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Check if the total amount can be met by any number of coins
    if dp[total] == float('inf'):
        return -1

    return dp[total]
