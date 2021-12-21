# Name:
# BTECH #:

import numpy as np

# *********  QUESTION 1  *********
# Using indexing, create the following matrix:
# Matrix 1
# [  0  0  1]
# [  0  9  1]
# [  0  0  1]

def createMatrix1():
    m = np.zeros(shape=(3, 3))
    m[:, 2] = 1
    m[1, 1] = 9
    return m


# *********  QUESTION 2  *********
# Using indexing, create the following matrix:
# Matrix 2
# [  0  0  0  7  0]
# [  1  1  1  1  1]
# [  3  4  5  4  3]
# [  1  1  1  1  1]
# [  7  0  0  0  0]

def createMatrix2():
    m = np.zeros(shape=(5,5))
    m[1::2, :] = 1
    m[0, 3] = 7
    m[4, 0] = 7
    m[2, :] = [3, 4, 5, 4, 3]
    return m


# *********  QUESTION 3  *********
# Using indexing and array methods, create the following matrix:
# Matrix 3
# [  1  0  3  0  3  0  0]
# [  0  1  0  2  2  2  0]
# [  4  4  1  4  4  4  4]
# [  0  0  0  1  0  0  0]
# [  9  9  9  0  1  0  0]
# [  9  9  9  0 10  1  0]
# [  9  9  9  0  0  0  1]

def createMatrix3():
    m = np.eye(7)
    m[2, :] = 4
    m[2, 2] = 1
    n = np.full((3, 3), 9)
    m[4:, :3] = n.copy()
    m[1, 3:6] = 2
    m[5, 4] = 10
    m[0, 2] = 3
    m[0, 4] = 3
    return m

