# Name: Hayden Hoopes
# Date: December 27, 2021

import numpy as np

def board_print(board):
    # Function by Jack C of Medium.com https://medium.com/codex/building-a-simple-sudoku-solver-in-python-with-numpy-1a8ea6f5bff5
    """
    Prints 9x9 numpy array input board in an easier to read format.
    """
    
    # Some basic checks
    assert board.shape == (9, 9)
    assert type(board) == np.ndarray
    
    # Convert array elements to strings
    board_str = board.astype(str)
    
    # Our row separator
    row_sep = '-'*25

    # Loop through 9 rows
    for i in range(9):
        
        # At each multiple of 3, print row separator
        if i % 3 == 0:
            print(row_sep)

        # Get row data
        row = board_str[i]

        # Format row of data with pipe separators at each end, and between each sub grid
        print('| '+' '.join(row[0:3])+' | '+' '.join(row[3:6])+' | '+' '.join(row[6:])+' |')

    # Print final row separator at bottom after loops finish
    print(row_sep)
