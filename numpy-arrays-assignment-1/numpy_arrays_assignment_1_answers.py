# Name: 
# BTECH #:

# This assignment uses automated tests. Feel free to run the tests yourself to check your work by executing
# python test_numpy_arrays_assignment_1.py  on the command line.

# Import numpy
import numpy as np



# ******************  QUESTION 1  ******************
# Imagine that you were given a data set with 5,000,000 rows and asked to analyze the temperatures. However,
# all of the temperatures are in Celsuis and you need to convert them to Fahrenheit, since you live in the U.S.
# Create two functions, one that uses regular Python loops and another that uses numpy arrays
# Compare the difference in computing time.
# Assume that the temperatures are given as a Python list of integers (ie. [16, 43, 99])

# This function uses loops to convert a list of temperatures in Celsius to temperatures in Fahrenheit
def celsiusToFahrenheitWithLoops(temperatures):
    for i in range(len(temperatures)):
        temperatures[i] = temperatures[i] * 9/5 + 32
    return temperatures


# This function uses NumPy arrays to convert a list of temperatures in Celsius to temperatures in Fahrenheit
def celsiusToFahrenheitWithArrays(temperatures):
    return np.array(temperatures) * 9/5 + 32

'''
    How much faster is it to convert temperatures using NumPy arrays compared to regular Python lists?

    ANSWER: Your answer here (run tests to find answer)
'''



# ******************  QUESTION 2  ******************
# Create a function that takes in two parameters: a width and a height. It then 
# returns an matrix of that size filled with random integers between 0 and 10.
def randomIntegerMatrix(width, height):
    return np.random.randint(10, size=(height, width))



# ******************  QUESTION 3  ******************
# Create a function that takes an integer and returns an identity matrix of that height and width.
def makeIdentityMatrix(integer):
    return np.eye(integer)