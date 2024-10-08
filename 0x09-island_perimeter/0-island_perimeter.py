#!/usr/bin/python3
""" Module solve the island perimeter problem """


def island_perimeter(grid):
    """ Function solves the island perimeter problem
    using a grid passed into it
    Return:
         the perimeter of the island described in grid
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                tile_count = 4
                try:
                    if grid[i][j + 1] == 1:
                        tile_count -= 1
                except IndexError:
                    pass
                try:
                    if grid[i + 1][j] == 1:
                        tile_count -= 1
                except IndexError:
                    pass
                if i != 0:
                    if grid[i - 1][j] == 1:
                        tile_count -= 1
                if j != 0:
                    if grid[i][j - 1] == 1:
                        tile_count -= 1
            else:
                tile_count = 0
            perimeter += tile_count
    return perimeter
