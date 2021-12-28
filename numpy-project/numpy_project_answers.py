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


def solveSudoku(grid):
    # 1. Make a copy of the sudoku matrix
    s = grid.copy()

    # if value is 0 or list, then run the algorithm
    stillGoing = True
    while stillGoing:
        changes = 0
        for row in range(9):
            for col in range(9):
                if s[row, col] == 0:
                    potentialValues = getSpotValues(s, row, col)
                    if len(potentialValues) == 1:
                        s[row, col] = potentialValues[0]
                        changes += 1
        
        if changes == 0:
            stillGoing = False
    return s


def getValuesInRow(grid, row):
    return [i for i in grid[row,:] if i != 0]


def getValuesInColumn(grid, col):
    return [i for i in grid[:,col] if i != 0]


def getValuesInBox(grid, row, col):
    topBound = (row // 3) * 3
    bottomBound = topBound + 3
    leftBound = (col // 3) * 3
    rightBound = leftBound + 3
    g = grid[topBound:bottomBound, leftBound:rightBound].flatten()

    return [i for i in g if i != 0]


def getSpotValues(grid, row, col):
    possibleValues = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    r = getValuesInRow(grid, row)
    c = getValuesInColumn(grid, col)
    b = getValuesInBox(grid, row, col)
    return list(possibleValues - set(r + c + b))
