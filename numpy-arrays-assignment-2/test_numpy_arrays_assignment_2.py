# Name: Hayden Hoopes
# Date: 12/20/2021

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
from numpy_arrays_assignment_2 import createMatrix1, createMatrix2, createMatrix3

class Test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("Checking matrices...\n")

    def test_matrix_1(self):
        m = createMatrix1()
        n = np.array([
            [0, 0, 1],
            [0, 9, 1],
            [0, 0, 1]
        ])
        self.assertIsNone(np.testing.assert_array_equal(m, n))

    def test_matrix_2(self):
        m = createMatrix2()
        n = np.array([
            [0, 0, 0, 7, 0],
            [1, 1, 1, 1, 1],
            [3, 4, 5, 4, 3],
            [1, 1, 1, 1, 1],
            [7, 0, 0, 0, 0]
        ])
        self.assertIsNone(np.testing.assert_array_equal(m, n))
    
    def test_matrix_3(self):
        m = createMatrix3()
        n = np.array([
            [1, 0, 3, 0, 3, 0, 0],
            [0, 1, 0, 2, 2, 2, 0],
            [4, 4, 1, 4, 4, 4, 4],
            [0, 0, 0, 1, 0, 0, 0],
            [9, 9, 9, 0, 1, 0, 0],
            [9, 9, 9, 0, 10, 1, 0],
            [9, 9, 9, 0, 0, 0, 1]
        ])
        self.assertIsNone(np.testing.assert_array_equal(m, n))
    

if __name__ == '__main__':
    unittest.main()