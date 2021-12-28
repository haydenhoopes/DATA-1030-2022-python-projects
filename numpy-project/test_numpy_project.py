# Name: Hayden Hoopes
# Date: 12/27/2021

# Import the required libraries
import unittest
import numpy as np
import random

'''
    DO NOT EDIT THIS FILE
    Run this file from the command line to test your code.
    An "E" indicates and error and an "F" indicates failed test. A "*" indicates a passed test.
    A different copy of this file will be run against your code to test it.
'''

# Import the student's code
from numpy_project import solveSudoku


class TestSudokuSolver(unittest.TestCase):

    def test_type(self):
        self.assertIsInstance(solveSudoku(createSudoku()), np.ndarray)

    def test_case_1(self):
        solution = np.array([
            [7, 2, 6, 5, 3, 8, 9, 1, 4], 
            [5, 8, 3, 4, 1, 9, 2, 6, 7], 
            [4, 9, 1, 7, 6, 2, 8, 3, 5], 
            [9, 1, 5, 2, 4, 6, 3, 7, 8], 
            [2, 6, 4, 8, 7, 3, 1, 5, 9], 
            [8, 3, 7, 9, 5, 1, 6, 4, 2], 
            [3, 7, 2, 1, 8, 5, 4, 9, 6], 
            [1, 5, 8, 6, 9, 4, 7, 2, 3], 
            [6, 4, 9, 3, 2, 7, 5, 8, 1]])

        sudoku = np.array([[0, 0, 0, 5, 3, 0, 0, 1, 4], [0, 0, 0, 0, 1, 9, 0, 6, 7], [0, 0, 1, 7, 6, 0, 8, 0, 0], [9, 0, 0, 0, 0, 0, 0, 7, 0], [2, 0, 4, 8, 0, 3, 0, 5, 0], [8, 0, 0, 0, 0, 1, 6, 0, 0], [0, 0, 0, 1, 0, 5, 4, 9, 0], [0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 9, 3, 0, 0, 0, 8, 1]])
        s = solveSudoku(sudoku)
        self.assertIsNone(np.testing.assert_array_equal(s, solution))

    def test_case_2(self):
        solution = np.array([
            [5, 3, 7, 1, 4, 8, 6, 9, 2], 
            [4, 8, 1, 2, 9, 6, 3, 5, 7], 
            [9, 6, 2, 7, 5, 3, 8, 4, 1], 
            [6, 2, 5, 4, 3, 7, 1, 8, 9], 
            [3, 7, 4, 9, 8, 1, 2, 6, 5], 
            [8, 1, 9, 5, 6, 2, 7, 3, 4], 
            [1, 9, 6, 3, 2, 5, 4, 7, 8], 
            [7, 4, 8, 6, 1, 9, 5, 2, 3], 
            [2, 5, 3, 8, 7, 4, 9, 1, 6]])

        sudoku = np.array([[5, 3, 7, 1, 4, 8, 0, 9, 2], [0, 0, 0, 2, 9, 0, 0, 0, 0], [9, 0, 0, 0, 0, 0, 8, 4, 0], [6, 2, 0, 0, 0, 0, 0, 0, 0], [0, 7, 4, 0, 8, 0, 2, 6, 5], [0, 0, 0, 5, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 0, 4, 7, 8], [0, 0, 0, 6, 0, 9, 0, 2, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]])
        s = solveSudoku(sudoku)
        self.assertIsNone(np.testing.assert_array_equal(s, solution))

    def test_case_3(self):
        solution = np.array([
            [7, 8, 4, 9, 3, 1, 6, 5, 2], 
            [1, 3, 9, 6, 5, 2, 4, 8, 7], 
            [2, 5, 6, 4, 8, 7, 9, 3, 1], 
            [5, 4, 2, 7, 9, 8, 1, 6, 3], 
            [3, 6, 1, 2, 4, 5, 7, 9, 8], 
            [8, 9, 7, 1, 6, 3, 2, 4, 5], 
            [9, 1, 8, 3, 2, 6, 5, 7, 4], 
            [6, 2, 3, 5, 7, 4, 8, 1, 9], 
            [4, 7, 5, 8, 1, 9, 3, 2, 6]])

        sudoku = np.array([[7, 0, 4, 9, 0, 0, 0, 0, 2], [0, 0, 9, 0, 0, 0, 4, 8, 0], [0, 5, 0, 0, 0, 7, 0, 3, 1], [0, 4, 2, 0, 9, 0, 0, 0, 3], [0, 0, 0, 2, 4, 0, 0, 0, 0], [8, 0, 0, 1, 0, 0, 2, 0, 0], [0, 0, 0, 0, 0, 6, 5, 7, 0], [0, 0, 3, 0, 7, 0, 0, 1, 9], [0, 0, 0, 8, 0, 0, 3, 0, 0]])
        s = solveSudoku(sudoku)
        self.assertIsNone(np.testing.assert_array_equal(s, solution))

    def test_case_4(self):
        solution = np.array([
            [2, 5, 9, 6, 7, 1, 8, 3, 4], 
            [6, 7, 1, 3, 4, 8, 9, 2, 5], 
            [3, 4, 8, 2, 5, 9, 1, 6, 7], 
            [8, 3, 7, 9, 2, 4, 5, 1, 6], 
            [9, 2, 4, 1, 6, 5, 7, 8, 3], 
            [1, 6, 5, 8, 3, 7, 4, 9, 2], 
            [7, 8, 6, 4, 9, 3, 2, 5, 1], 
            [5, 1, 2, 7, 8, 6, 3, 4, 9], 
            [4, 9, 3, 5, 1, 2, 6, 7, 8]])

        sudoku = np.array([[0, 5, 0, 0, 0, 0, 8, 3, 0], [0, 0, 0, 0, 4, 0, 9, 0, 0], [3, 0, 8, 0, 0, 9, 0, 6, 0], [0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 8, 3], [1, 6, 5, 8, 0, 0, 0, 0, 2], [0, 0, 6, 0, 9, 3, 0, 5, 0], [0, 0, 0, 0, 0, 6, 0, 0, 9], [4, 9, 0, 0, 1, 2, 0, 0, 8]])
        s = solveSudoku(sudoku)
        self.assertIsNone(np.testing.assert_array_equal(s, solution))

    def test_case_5(self):
        solution = np.array([
            [2, 7, 3, 6, 8, 5, 1, 4, 9], 
            [6, 8, 5, 9, 4, 1, 3, 7, 2], 
            [9, 4, 1, 2, 7, 3, 5, 8, 6], 
            [5, 2, 8, 1, 6, 4, 7, 9, 3], 
            [3, 9, 7, 5, 2, 8, 4, 6, 1], 
            [1, 6, 4, 3, 9, 7, 8, 2, 5], 
            [8, 3, 2, 4, 5, 6, 9, 1, 7], 
            [4, 5, 6, 7, 1, 9, 2, 3, 8], 
            [7, 1, 9, 8, 3, 2, 6, 5, 4]])

        sudoku = np.array([[0, 0, 0, 0, 0, 5, 0, 4, 9], [0, 8, 0, 0, 4, 1, 3, 0, 2], [9, 0, 0, 0, 0, 0, 5, 0, 0], [0, 2, 8, 0, 6, 0, 0, 9, 3], [0, 0, 0, 5, 0, 0, 0, 6, 0], [0, 0, 0, 3, 0, 7, 8, 0, 0], [8, 0, 2, 0, 0, 0, 0, 1, 0], [0, 5, 0, 7, 0, 9, 0, 3, 0], [0, 0, 9, 0, 0, 0, 6, 0, 0]])
        s = solveSudoku(sudoku)
        self.assertIsNone(np.testing.assert_array_equal(s, solution))


if __name__ == '__main__':
    unittest.main()