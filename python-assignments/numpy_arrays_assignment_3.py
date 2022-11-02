# Name:
# BTECH #:

# Import the NumPy library here
# Your code here
import numpy as np


# Use the array below in the following questions.
numbers = np.array([12, 9, 15, 16, 11, 6, 11, 9, 2, 9, 10, 16, 19, 1, 8])


# ********  QUESTION 1  ********
# Print a boolean array that gives a series of True/False values related to 
# whether or not the number 11 appears in the `numbers` array.
# You should get the answer: [False False False False True False True False False False False False False False False]

# Your code here


# ********  QUESTION 2  ********
# Print a boolean array that gives a series of True/False values related to
# when the values in `numbers` are less than 6 or greater than 10.
# You should get the answer: [ True False True True True False True False True False False True True True False]

# Your code here


# ********  QUESTION 3  ********
# Print a boolean array that gives a series of True/False values related to
# when the values in `numbers` are not equal to 9.
# You should get the answer: [ True False True True True True True False True False True True True True True]

# Your code here


# ********  QUESTION 4  ********
# Print a boolean array that gives a series of True/False values related to
# when the values in `numbers` ARE equal to 9.
# You should get the answer: [False True False False False False False True False True False False False False False]

# Your code here


# ********  QUESTION 5  ********
# Filter using the `where()` function to get an array that only includes values of 9. 
# You should get the answer: [9 9 9]

# Your code here


# ********  QUESTION 6  ********
# Filter WITHOUT using the `where()` function to get an array that only includes values of 9.
# You should get the answer: [9 9 9]

# Your code here


# ********  QUESTION 7  ********
# Filter the `numbers` array (you can choose to use where() or to not use where()) to get an array with integers that are
# evenly divisible by 3.
# You should get the answer: [12  9 15  6  9  9]

# Your code here


# ********  QUESTION 8  ********
# Filter the `numbers` array (you can choose to use where() or to not use where()) to get an array with integers that are
# evenly divisible by 4.
# You should get the answer: [12 16 16  8]

# Your code here


# ********  QUESTION 9  ********
# Get a filtered array of `numbers` greater than 5 and less than 11. Print out the array.
# You should get the answer: [ 9  6  9  9 10  8]

# Your code here


# ********  QUESTION 10  ********
# Get a filtered array of `numbers` less than 5 or greater than 11. Print out the array.
# You should get the answer: [12 15 16  2 16 19  1]

# Your code here


# ********  QUESTION 11  ********
# Get a filtered array of `numbers` less than 5 and greater than 11. Print out the array.

# Your code here


# What did this code return?  Why?

''' Your answer here. '''

# ********  QUESTION 12  ********
# Get a filtered array of `numbers` either not divisible by 3 or are greater than 14.
# You should get the answer: [15 16 11 11  2 10 16 19  1  8]

# Your code here


# Use the following 2-dimensional list to answer the questions below.
numbers_2D = np.array([[16, 16,  6,  1,  4],
                       [15, 10,  7, 15, 14],
                       [ 5, 15,  7,  6, 17],
                       [ 8,  4,  2,  2,  2],
                       [ 3, 15,  4, 12,  1]])


# ********  QUESTION 13  ********
# Create a filter named `filt` that looks for items in the `numbers_2D` array greater than 10.
# It should look something like `filt = a > #`. Print out the filt variable.
# You should get the answer: [[ True  True False False False]
#                             [ True False False  True  True]
#                             [False  True False False  True]
#                             [False False False False False]
#                             [False  True False  True False]]

# Your code here


# ********  QUESTION 14  ********
# Why is a matrix of True/False values returned?

''' Your answer here. '''


# ********  QUESTION 15  ********
# Use the `filt` variable as the filter to get an array of numbers from the `numbers_2D` array. 
# (These values should all be greater than 10) This is accomplished by passing in the variable `filt` to the square brackets 
# This looks like `array[ filt ]`.
# Don't worry, working with 2-dimensional arrays is just as easy as working with 1-dimensional arrays!

# Your code here


# ********  QUESTION 16  ********
# What kind of array got printed out in the previous question (1-dimensional or 2-dimensional)? Why do you think this is?

''' Your answer here. '''
