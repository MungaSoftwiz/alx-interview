#!/usr/bin/python3
""" Module to solve rotating matrix """


def rotate_2d_matrix(matrix):
    """ Rotates an n X n matrix 90 degrees function
    Return:
        None as matrix will be edited in place
    """
    if len(matrix) < 1:
        return
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
