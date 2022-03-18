# Name: 
# BTECH #:


# ******************  QUESTION 1  ******************
# Import the numpy library under the alias np. Run this Python file to make sure that you have it installed
# and imported correctly. You should not see any output.

import numpy as np


# ******************  QUESTION 2  ******************
# Create a new NumPy array called myFirstArray by passing in a list of integers to the array() function. Do
# not save the list as a variable. Pass it directly in to the function. Add at least 3 integers.

myFirstArray = np.array([1, 2, 3])


# ******************  QUESTION 3  ******************
# Create a new NumPy array called mySecondArray by creating a list of strings, saving it to a variable, and
# then passing the variable into the array() function. Add at least three strings.

someStrings = ['hello', 'there', 'world']
mySecondArray = np.array(someStrings)


# ******************  QUESTION 4  ******************
# Print out the sum, mean, max, and minimum of the following array. Turn it into a NumPy array and use the
# array methods to perform these operations.
numbers = [37, 27, 22, 60, 69, 31, 25, 31, 16, 12, 70,  3, 87, 95, 75, 57, 27, 32, 6, 16, 22, 92, 41, 75, 88, 93, 76]
numberArray = np.array(numbers)

# Sum
print(numberArray.sum())

# Mean
print(numberArray.mean())

# Max
print(numberArray.max())

# Min
print(numberArray.min())


# ******************  QUESTION 5  ******************
# Create a NumPy array containing numbers 1-10. Use multiplication on this array to get a new array that
# contains each of these numbers squared. Print out the array of squares when you finish.
number = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(number ** 2)


# ******************  QUESTION 6  ******************
# Get the shape of the following array and print it out.
bigList = [[2, 3, 7, 5, 6, 9, 3, 6, 5],
           [6, 5, 9, 1, 2, 1, 8, 8, 9],
           [2, 7, 5, 4, 8, 2, 3, 4, 9],
           [8, 1, 6, 1, 1, 7, 4, 8, 1],
           [5, 9, 8, 9, 2, 2, 5, 6, 7],
           [1, 1, 4, 6, 3, 1, 6, 1, 4],
           [3, 5, 5, 4, 1, 7, 3, 3, 5],
           [3, 5, 8, 1, 3, 8, 6, 2, 1],
           [5, 4, 2, 9, 5, 1, 6, 2, 3],
           [6, 1, 2, 8, 2, 5, 7, 1, 6],
           [2, 7, 2, 7, 4, 8, 7, 4, 9],
           [9, 9, 2, 7, 4, 5, 3, 9, 7],
           [3, 4, 9, 5, 3, 3, 6, 9, 7]]

bigArray = np.array(bigList)
print(bigArray.shape)


# ******************  QUESTION 7  ******************
# Recreate the matrix below using the `full()` function. Print it out.
#   [ 5 5 5 ]
#   [ 5 5 5 ]
#   [ 5 5 5 ]   
#   [ 5 5 5 ]
#   [ 5 5 5 ]

fives = np.full((5, 3), 5)
print(fives)


# ******************  QUESTION 8  ******************
# Imagine that you were given a data set with 5,000,000 rows and asked to analyze the temperatures. However,
# all of the temperatures are in Celsuis and you need to convert them to Fahrenheit, since you live in the U.S.
# Create two functions, one that uses regular Python loops and another that uses numpy arrays to convert each
# number in the list to Fahrenheit. Your function should `return` a new list/NumPy array AND print out the
# list/array. Assume that the temperatures are given as a list of integers.

# The formula for converting a temperature from Celsius to Fahrenheit is `temperature * 9/5 + 32`.

# Call the functions once after you create them. You can use this list of temperatures to test. Note that in 
# Fahrenheit, the -40C = -40F, 0C = 32F, and 100C = 212F.
temperaturesInCelsius = [-40, 0, 100]

# This function uses loops to convert a list of temperatures in Celsius to temperatures in Fahrenheit
def celsiusToFahrenheitWithLoops(temperatures):
    for i in range(len(temperatures)):
        temperatures[i] = temperatures[i] * 9/5 + 32
    print(temperatures)
    return temperatures

celsiusToFahrenheitWithLoops(temperaturesInCelsius)


# This function uses NumPy arrays to convert a list of temperatures in Celsius to temperatures in Fahrenheit.
# Remember that the temperatures are given as a list, so you need to convert them to a NumPy array.
def celsiusToFahrenheitWithArrays(temperatures):
    temps = np.array(temperatures) * 9/5 + 32
    print(temps)
    return temps

celsiusToFahrenheitWithArrays(temperaturesInCelsius)


# ******************  QUESTION 9  ******************
# Create a function that takes in two parameters: a width and a height. It then returns an matrix of that 
# size filled with random integers between 0 and 10. Print out the array as well.
def randomIntegerMatrix(width, height):
    return np.random.randint(10, size=(height, width))


# ******************  QUESTION 10  ******************
# Create a function that takes an integer and returns an identity matrix of that height and width. Make the
# function print out the array AND return it.
def makeIdentityMatrix(integer):
    return np.eye(integer)
