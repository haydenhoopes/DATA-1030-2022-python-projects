# Name: 
# BTECH #:

# SUDOKU SOLVER
# Sudoku is a Japanese number game that uses a 9x9 grid of integers from 1 to 9 to create a unique 
# pattern in which each number occurs once in each row, once in each column, and once in each of the 
# nine 3x3 boxes on the grid.

# In this Sudoku solver, the number 0 represents an empty space.

# Import numpy
import numpy as np

# Import `board_print()` function (for formatting the puzzle when printing)
from sudoku_utils import board_print

# This is an example sudoku puzzle. Use it for reference and testing.
sudoku = np.array([
    [ 0, 1, 0, 0, 3, 8, 0, 6, 0],
    [ 0, 0, 0, 0, 0, 1, 0, 4, 5],
    [ 5, 9, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 3, 9, 0, 1, 0, 0],
    [ 6, 5, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 1, 6, 0, 0, 2, 0],
    [ 0, 0, 0, 6, 1, 4, 0, 0, 0],
    [ 0, 0, 7, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 8, 0, 9]
])

# board_print(sudoku) # Uncomment this to see a formatted print out of the puzzle


# ********  Function 1  ********
# Create a function called `get_values_in_row()`. This function should accept (1) a 9x9 grid of numbers
# (ie. the Sudoku puzzle) and (2) a row number. It should perform the following steps:
#   1. Create an empty list called `values_in_row`.
#   2. Use a for loop to iterate through each number in the row. `for number in grid[row,:]`.
#   3. Inside the for loop, use an if statement to determine if each number is equal to 0 or not.
#       - If the number is equal to 0, do nothing.
#       - Else (if the number is not 0) add it to the list `values_in_row`.
#   4. After the for loop, return the list `values_in_row`.

def get_values_in_row(grid, row):
    values_in_row = []
    for number in grid[row,:]:
        if number != 0:
            values_in_row.append(number)
    return values_in_row

# TRY IT OUT: Write code below this line to test out the `get_values_in_row()` function three times. Comment it 
# out when you finish testing.
# print(get_values_in_row(sudoku, 0)) # Get values in the top row (0). Should return [5, 7, 3]


# ********  Function 2  ********
# Create a function called `get_values_in_column()`. This function should accept (1) a 9x9 grid of numbers
# (ie. the Sudoku puzzle) and (2) a column number. It should perform the following steps:
#   1. Create an empty list called `values_in_column`.
#   2. Use a for loop to iterate through each number in the column. `for number in grid[:,column]`.
#   3. Inside the for loop, use an if statement to determine if each number is equal to 0 or not.
#       - If the number is equal to 0, do nothing.
#       - Else (if the number is not 0) add it to the list `values_in_column`.
#   4. After the for loop, return the list `values_in_column`.

def get_values_in_column(grid, col):
    values_in_column = []
    for number in grid[:,col]:
        if number != 0:
            values_in_column.append(number)
    return values_in_column

# TRY IT OUT: Write code below this line to test out the `get_values_in_column()` function three times. Comment it 
# out when you finish testing.
# print(get_values_in_column(sudoku, 0)) # Get values in the leftmost column (0). Should return [8, 7, 5, 2, 9]


# ********  Function 3  ********
# Create a function called `get_values_in_box()`. This function should accept (1) a 9x9 grid of numbers
# (ie. the Sudoku puzzle), (2) a row number, and (3) a column number. The row number and column number indicate
# the position of each value in the Sudoku puzzle. It should perform the following steps:
#   1. Get the boundaries of the box given a row and column.
#       - Get the top_bound.
#       - Get the bottom_bound.
#       - Get the left_bound.
#       - Get the right_bound.
#   2. Get a slice of the sudoku puzzle using the `grid` variable, setting the boundaries inside square brackets
#      with colons between them. Don't forget to add one (+1) to bottom_bound and right_bound since the second
#      number of NumPy slices is not inclusive. Save the slice with the name `little_grid`.
#   3. Create a new list called `values_in_box`.
#   4. Use a for loop to iterate through each number in the row of the `little_grid`. `for row in little_grid`. 
#   5. Use another for loop inside of the first one that iterates through each column in the row. `for col in row`.
#   6. Inside the inner for loop, use an if statement to determine if the number at position little_grid[row, col]
#      is equal to 0 or not.
#       - If the number is equal to 0, do nothing.
#       - Else (if the number is not 0), add it to the list `values_in_box`.
#   7. After both for loops, return the list `values_in_box`.

def get_values_in_box(grid, row, col):
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

# TRY IT OUT: Write code below this line to test out the `get_values_in_box()` function three times. Comment it 
# out when you finish testing.
# print(get_values_in_box(sudoku, 0, 0)) # Get values in the top left box (position [0, 0]). Should return [8, 7]


# ********  Function 4  ********
# Create a function called `get_spot_values()`. This function should accept (1) a 9x9 grid of numbers (ie.
# the Sudoku puzzle), (2) a row number, and (3) a column number. The row number and column number indicate the
# position of a single value in the Sudoku puzzle. This function should perform the following steps:
#   1. Create a list that is prepopulated with numbers 1 through 9 called `numbers`.
#   2. Call the function `get_values_in_row()`, passing in the grid of numbers and the row from the
#      `get_spot_values()` parameters. Save the results of this function to a variable `values_in_row`.
#   3. Call the function `get_values_in_column()`, passing in the grid of numbers and the column from the
#      `get_spot_values()` parameters. Save the results of this function to a variable `values_in_column`.
#   4. Call the function `get_values_in_box()`, passing in the grid of numbers and the row and column from the
#      `get_spot_values()` parameters. Save the results of this function to a variable `values_in_box`.
#   5. Create an empty list called `possibilities`. This list will store each number that a given space could
#      possibly be.
#   6. Use a for loop to iterate through each number in `numbers`. `for number in numbers:`
#   7. Inside the for loop, use an if statement to determine if each number is is `values_in_row`, 
#      `values_in_column`, and `values_in_box`. If the number is not in any of these lists, then add it to the
#      list `possibilities`.
#   8. After the for loop, return the list `possibilities`.

def get_spot_values(grid, row, col):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    values_in_row = get_values_in_row(grid, row)
    values_in_column = get_values_in_column(grid, col)
    values_in_box = get_values_in_box(grid, row, col)

    possibilities = []
    for number in numbers:
        if number not in values_in_row and number not in values_in_column and number not in values_in_box:
            possibilities.append(number)
    return possibilities

# TRY IT OUT: Write code below this line to test out the `get_spot_values()` function three times. Comment it 
# out when you finish testing.
# print(get_spot_values(sudoku, 0, 0)) # Get potential values for the top-left number. Should return [1, 4, 6]


# ********  Function 5  ********
# Create a function called `solve_sudoku()`. This function should accept a 9x9 NumPy matrix that represents
# an incomplete Sudoku puzzle. The function should do the following:
# PROVIDED FOR YOU
#   1. Create a variable `still_going` that is set to True. This variable will be used to tell the while loop
#      to either keep going (True) or stop (False).
#   2. Use a while loop to iterate through the Sudoku puzzle until it is completely solved. Use the `still_going`
#      variable as the condition of the while loop.
#   3. Create a variable `changes` set equal to 0 at the beginning of the while loop. We have to keep track of 
#      how many changes we make each time we iterate through the Sudoku puzzle. If we don't make any changes in
#      an iteration, that means that the puzzle has been completely solved.
#   4. Use a for loop to iterate through numbers 0-9 (not inclusive) and call each iteration `row`. This
#      represents each row of the Sudoku puzzle.
#   5. Use another for loop inside the first one that iterates through numbers 0-9 (not inclusive) and call each
#      iteration `col`. This represents each column of each row.

# YOU DO THIS
#   6. Use an if statement to determine if, for each row and column (ie. each individual cell of the Sudoku puzzle)
#      the number is equal to 0. If it is, then use the function `get_spot_values()` to determine which values it
#      could possibly be. Save the results of the `get_spot_values()` function to a variable `potential_values`.
#   7. Still inside this if statement, use another if statement to determine the length of `potential_values`. If
#      the length is 1, that means that there is only one possibility for the current value. Thus, if the length of
#      `potential_values` is 1, modify the Sudoku grid at position [row, col] to be equal to the first item in
#      `potential_values`.
#   8. If the length was equal to 1, add 1 (+= 1) to the variable `changes`.

# PROVIDED FOR YOU
#   9. After both for loops, determine if `changes` was equal to 0. If it wasn't, do nothing (the while loop will
#      run again). If `changes` was equal to 0, no changes were made and the Sudoku puzzle has been solved. If
#      `changes` was equal to 0, set the variable `still_going` to False.
#  10. After the while loop, use the `board_print()` function to print out the solved Sudoku puzzle.
#  11. Return the finished Sudoku puzzle as a NumPy array.

def solve_sudoku(grid):
    still_going = True
    while still_going:
        changes = 0
        for row in range(9):
            for col in range(9):
                if grid[row,col] == 0:
                    potential_values = get_spot_values(grid, row, col)
                    print(potential_values)
                    if len(potential_values) == 1:
                        grid[row, col] = potential_values[0]
                        changes += 1
        if changes == 0:
            still_going = False
    board_print(grid)
    return grid

# TRY IT OUT: Uncomment the code below to check your work on the Sudoku solver.
solve_sudoku(sudoku) # Solves the Sudoku puzzle. Should return a finished Sudoku puzzle.

# -------------------------
# | 1 9 2 | 4 6 8 | 5 7 3 |
# | 8 5 3 | 1 2 7 | 4 9 6 |
# | 7 6 4 | 9 5 3 | 8 1 2 |
# -------------------------
# | 5 8 9 | 7 3 6 | 1 2 4 |
# | 4 7 1 | 8 9 2 | 3 6 5 |
# | 2 3 6 | 5 4 1 | 7 8 9 |
# -------------------------
# | 9 1 5 | 6 7 4 | 2 3 8 |
# | 3 4 7 | 2 8 9 | 6 5 1 |
# | 6 2 8 | 3 1 5 | 9 4 7 |
# -------------------------
