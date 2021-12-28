# Name: 
# BTECH #:

# SUDOKU SOLVER
# Sudoku is a Japanese number game that uses a 9x9 
# grid of integers from 1 to 9 to create a unique 
# pattern in which each number occurs once in each row, 
# once in each column, and once in each of the nine 3x3 boxes on the grid.

# In this Sudoku solver, the number 0 represents an empty space.

# Import numpy
# Your code here

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
    # Your code here
    return 


def getValuesInRow(grid, row):
    # Your code here
    return


def getValuesInColumn(grid, col):
    # Your code here
    return


def getValuesInBox(grid, row, col):
    # Your code here
    return


def getSpotValues(grid, row, col):
    # Your code here
    return
