#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem"""


import sys


def is_safe(board, row, col, N):
    # Check if a queen can be placed at position (row, col)
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check if there is a queen in the upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(N):
    # Check if N is a number
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [['.' for _ in range(N)] for _ in range(N)]
    solutions = []

    def backtrack(row):
        # Base case: all queens are placed
        if row == N:
            solution = [''.join(row) for row in board]
            solutions.append(solution)
            return

        # Try placing a queen in each column of the current row
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    backtrack(0)

    # Print the solutions
    for solution in solutions:
        for row in solution:
            print(row)
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    solve_nqueens(sys.argv[1])
