#!/usr/bin/python3

"""import sys"""
import sys


def is_valid(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n, row, board, solutions):
    """Use backtracking to find all solutions for the N queens problem."""
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)
            board[row] = -1


def print_solutions(solutions):
    """Print the solutions in the required format."""
    for solution in solutions:
        formatted_solution = [[i, solution[i]] for i in range(len(solution))]
        print(formatted_solution)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [-1] * n
    solve_nqueens(n, 0, board, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
