# Hayden Hoopes
# December 27, 2021

import numpy as np
from numpy_project import *
from sudoku_utils import board_print

def createSudoku():
    # Function adapted from code by Alain T. of Stack Overflow https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python
    base  = 3
    side  = base*base

    # pattern for a baseline valid solution
    def pattern(r,c): return (base*(r%base)+r//base+c)%side

    # randomize rows, columns and numbers (of valid base pattern)
    from random import sample
    def shuffle(s): return sample(s,len(s)) 
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    board = np.array([ [nums[pattern(r,c)] for c in cols] for r in rows ], dtype="int")
    empty_board = board.copy()

    squares = side*side
    empties = squares * 3//4
    for p in sample(range(squares),empties):
        row = p//side
        col = p % side
        
        tempMemory = empty_board[row, col]
        empty_board[row, col] = 0
        testS = solveSudoku(empty_board)
        if 0 in testS:
            empty_board[row, col] = tempMemory

    return empty_board
