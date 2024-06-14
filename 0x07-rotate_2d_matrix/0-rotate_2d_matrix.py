#!/usr/bin/python3
""" 2d matrix that turn 90
    degree clockwise
"""


def rotate_2d_matrix(matrix):
    """matrix[[1, 2, 3], 3 6 9
              [4, 5, 6]  2 5 8
              [7, 8, 9]] 1 4 7

                         9 8 7
                         6 5 4
                         3 2 1

                         7 4 1
                         8 5 2
                         9 6 3

        outer_list_size = 3
        inner_list_size = 3
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(len(matrix)):
        matrix[i].reverse()
