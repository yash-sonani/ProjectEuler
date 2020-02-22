#!/bin/python3

import sys

grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)

max_product = 0

for row in range(20):
    right = 0
    right_down = 0
    left_down = 0
    down = 0
    for column in range(20):

        if column < 17:
            right = grid[row][column] * grid[row][column + 1] * grid[row][column + 2] * grid[row][column + 3]

        if row < 17 and column < 17:
            right_down = grid[row][column] * grid[row + 1][column + 1] * grid[row + 2][column + 2] * grid[row + 3][
            column + 3]

        if row < 17:
            down = grid[row][column] * grid[row + 1][column] * grid[row + 2][column] * grid[row + 3][column]

        if row < 17 and column > 2 :
            left_down = grid[row][column] * grid[row + 1][column - 1] * grid[row + 2][column - 2] * grid[row + 3][column - 3]

        max_product = max(right, right_down, down, left_down, max_product)

print(max_product)
