#!/usr/bin/python3

"""
    Declare a function called pascal_triangle
"""


def pascal_triangle(n):
    """
        Function that returns a list of lists of integers
        representing the Pascal’s triangle of n

        Par:
            n (int): The number of rows of Pascal's triangle to generate.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Create a row with all elements as 1
        row = [1] * (i + 1)
        # Calculate the inner elements
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)

    return triangle
