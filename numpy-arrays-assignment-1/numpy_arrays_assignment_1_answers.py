# Name: 
# BTECH #:


# ******************  QUESTION 1  ******************
# Import the numpy library under the alias np. Run this Python file to make sure that you have it installed
# and imported correctly. You should not see any output.

import numpy as np


# ******************  QUESTION 2  ******************
# Create a new NumPy array called my_first_array by passing in a list of at least integers to the array() function.
# Save the array as my_first_array, but do not save the list as a variable. Pass it directly in to the function. 
# This can be done in one line of code.

my_first_array = np.array([1, 2, 3, 4, 5])


# ******************  QUESTION 3  ******************
# Create a list of strings called list_of_strings with at least three strings. 
# Then create a new NumPy array called my_second_array by passing list_of_strings into the array() function.

list_of_strings = ["hello", "there", "world"]
my_second_array = np.array(list_of_strings)


# ******************  QUESTION 4  ******************
# Turn 'numbers' into an array. Then use array functions to print out the sum, mean, max, and minimum of the following array.
numbers = [37, 27, 22, 60, 69, 31, 25, 31, 16, 12, 70, 3, 87, 95, 75, 57, 27, 32, 6, 16, 22, 92, 41, 75, 88, 93, 76]

# Convert list to array
numbers = np.array(numbers)

# Sum
print(numbers.sum())

# Mean
print(numbers.mean())

# Max
print(numbers.max())

# Min
print(numbers.min())


# ******************  QUESTION 5  ******************
# Create a 5 by 3 NumPy array containing random numbers between 1 and 10. Print this array.
# Use a mathematical operation on this array to get a new array that contains each of these numbers squared. 
# Print out the array of squares when you finish.

random_ints = np.random.randint(1, 10, (5, 3))
print(random_ints)
print(random_ints ** 2)


# ******************  QUESTION 6  ******************
# Get the shape of the following array and print it out. Note that it is currently a list, so you should
# convert it to a NumPy array first.

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

print(np.array(bigList).shape)


# ******************  QUESTION 7  ******************
# Recreate the matrix below using the `full()` function. Print it out.
#  [[5 5 5]
#   [5 5 5]
#   [5 5 5]   
#   [5 5 5]
#   [5 5 5]]

print(np.full((5, 3), 5))


# ******************  QUESTION 8  ******************
# Imagine that you were given a data set with 5 million rows and asked to analyze the temperatures. However,
# all of the temperatures are in Celsuis and you need to convert them to Fahrenheit, since you live in the U.S.
# Create two functions, one that uses regular Python loops and another that uses numpy arrays to convert each
# number in the list to Fahrenheit. Your function should `return` a new list/NumPy array AND print out the
# list/array. Assume that the temperatures are given as a list of integers.

# ALL WORK SHOULD BE DONE INSIDE THE FUNCTIONS.

# The formula for converting a temperature from Celsius to Fahrenheit is 
# CelsiusTemp * 9/5 + 32 = FahrenheitTemp

# Call the functions once after you create them. Use this list of temperatures to test. 
# Note that in Fahrenheit, the -40C = -40F, 0C = 32F, and 100C = 212F.
c_temps = [-40, 0, 100]

# This function uses loops to convert a list of temperatures in Celsius to temperatures in Fahrenheit
def celsius_to_fahrenheit_with_loops(temperatures):
    f_temps = []
    for x in temperatures:
        f_temps.append(x * 9/5 + 32)
    print(f_temps)
    return f_temps

# Uncomment this next line to test your function
celsius_to_fahrenheit_with_loops(c_temps)

# This function uses NumPy arrays to convert a list of temperatures in Celsius to temperatures in Fahrenheit.
# Remember that the temperatures are given as a list, so you need to convert them to a NumPy array.
def celsius_to_fahrenheit_with_arrays(temperatures):
    f_temps = np.array(temperatures) * 9/5 + 32
    print(f_temps)
    return f_temps

celsius_to_fahrenheit_with_arrays(c_temps)

# ******************  QUESTION 9  ******************
# Create a function that takes in two parameters: row and column. 
# It then prints a matrix of that size fills it with random integers between 0 and 10. 
# Test this function with the values 3 (for row) and 15 (for column).
def random_integer_matrix(row, column):
    print(np.random.randint(1, 10, (row, column)))

random_integer_matrix(3, 15)


# ******************  QUESTION 10  ******************
# Create a function that takes an integer and returns an identity matrix of that height and width. 
# Make the function print out the array AND return it.
# Test the function with the value of 7.
def make_identity_matrix(integer):
    i = np.eye(integer)
    print(i)
    return i
