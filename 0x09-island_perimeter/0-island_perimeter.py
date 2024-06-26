#!/usr/bin/python3

"""declare a funcction """


def island_perimeter(grid):
    """ function that returns the perimeter
        of the island in the grid

        Args:
          (grid) - is a list of list of integers:
                   0 represents water
                   1 represents land
        Return:
          - returns the perimeter of the island described in grid
    """
    perimeter = 0

    if len(grid) == 0:
        return perimeter

    for row in range(len(grid)):
        for comn in range(len(grid[row])):
            if grid[row][comn] == 1:
                perimeter += 4

                if row > 0 and grid[row - 1][comn] == 1:
                    perimeter -= 2

                if comn > 0 and grid[row][comn - 1] == 1:
                    perimeter -= 2
    return perimeter
