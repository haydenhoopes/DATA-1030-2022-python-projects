# Name: 
# BTECH #:

# SUDOKU SOLVER
# Sudoku is a Japanese number game that uses a 9x9 
# grid of integers from 1 to 9 to create a unique 
# pattern in which each number occurs once in each row, 
# once in each column, and once in each of the nine 3x3 boxes on the grid.

# In this Sudoku solver, the number 0 represents an empty space.

# Import numpy
import numpy as np

# Import sudoku utilities (for formatting and creating new Sudokus)
from sudoku_utils import board_print

# This is an example sudoku puzzle. Use it for reference and testing.
sudoku = np.array([
    [ 0, 0, 0, 0, 0, 0, 5, 7, 3],
    [ 8, 0, 0, 0, 2, 0, 0, 0, 0],
    [ 7, 0, 0, 9, 0, 0, 8, 1, 0],
    [ 5, 8, 0, 7, 0, 6, 0, 0, 0],
    [ 0, 0, 1, 8, 0, 0, 0, 6, 0],
    [ 2, 3, 0, 0, 4, 0, 0, 0, 9],
    [ 9, 1, 5, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 8, 0, 6, 0, 1],
    [ 0, 0, 0, 0, 0, 0, 0, 4, 0]
])

# board_print(sudoku) # Uncomment this to see a formatted print out of the puzzle


def solveSudoku(grid):
    still_going = True
    while still_going:
        changes = 0
        for row in range(9):
            for col in range(9):
                if grid[row,col] == 0:
                    potentialValues = getSpotValues(grid, row, col)
                    if len(potentialValues) == 1:
                        grid[row, col] = potentialValues[0]
                        changes += 1
        if changes == 0:
            still_going = False
    board_print(grid)
    return grid


def getValuesInRow(grid, row):
    values_in_row = []
    for number in grid[row,:]:
        if number != 0:
            values_in_row.append(number)
    return values_in_row


def getValuesInColumn(grid, col):
    values_in_column = []
    for number in grid[:,col]:
        if number != 0:
            values_in_column.append(number)
    return values_in_column


def getValuesInBox(grid, row, col):
    top_bound = (row // 3) * 3
    bottom_bound = top_bound + 3
    left_bound = (col // 3) * 3
    right_bound = left_bound + 3

    little_grid = grid[top_bound:bottom_bound, left_bound:right_bound]
    values_in_box = []
    for row in range(3):
        for col in range(3):
            if little_grid[row,col] != 0:
                values_in_box.append(little_grid[row,col])
    return values_in_box

def getSpotValues(grid, row, col):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    values_in_row = getValuesInRow(grid, row)
    values_in_column = getValuesInColumn(grid, col)
    values_in_box = getValuesInBox(grid, row, col)

    possibilities = []
    for number in numbers:
        if number not in values_in_row and number not in values_in_column and number not in values_in_box:
            possibilities.append(number)
    return possibilities

solveSudoku(sudoku)