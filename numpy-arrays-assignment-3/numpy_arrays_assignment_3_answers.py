# Name:
# BTECH #:

# Import numpy
import numpy as np

# Get three pseudo-random sets of integers between -100 and 100
# np.random.seed(1) # UNCOMMENT ME
# array = np.random.randint(-100, 101, 100) # UNCOMMENT ME: You can use this array to test your functions


# ********  QUESTION 1  ********
# Build a function that takes in an array and two integers and returns an array of items greater than the first number and less than the second number?
def getNumbersBetween(array, lowerNumber, higherNumber):
    return array[ (array > lowerNumber) & (array < higherNumber) ]



# ********  QUESTION 2  ********
# Build a function that takes in an array of integers and returns all of the negative numbers EXCEPT for -57
def negativeNumbersExceptNegative57(array):
    return array[ (array < 0) & (array != -57) ]



# ********  QUESTION 3  ********
# Write a function that takes an array and a number, and retrieves an array of each number immediately to the left and right of that number. 
# The order of the values is not important. Remember that you can join two arrays together using the NumPy
# concatenate function, where the first argument is a tuple that contains each array to be merged.
# np.concatenate((arr1, arr2))
def leftAndRight(array, num):
    indexes = np.where(array == num)[0]
    leftIndexes = indexes - 1
    rightIndexes = indexes + 1
    
    return np.concatenate((array[ rightIndexes ], array[ leftIndexes ]))
