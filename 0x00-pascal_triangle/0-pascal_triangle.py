#!/usr/bin/python3
"""
Pascal triangle algorithm
"""


def pascal_triangle(n):
    """ Returns a list of lists of integers representing the Pascal’s triangle of n
    Returns: Empty list if n <= 0
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        # First element, each row
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        # Last element, each row
        row.append(1)
        triangle.append(row)

    return triangle
