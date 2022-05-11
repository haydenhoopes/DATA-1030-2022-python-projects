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

print(numbers == 11)


# ********  QUESTION 2  ********
# Print a boolean array that gives a series of True/False values related to
# when the values in `numbers` are less than 6 or greater than 10.
# You should get the answer: [ True False True True True False True False True False False True True True False]

print((numbers < 6) | (numbers > 10))


# ********  QUESTION 3  ********
# Print a boolean array that gives a series of True/False values related to
# when the values in `numbers` are not equal to 9.
# You should get the answer: [ True False True True True True True False True False True True True True True]

print(~(numbers == 9))


# ********  QUESTION 4  ********
# Print a boolean array that gives a series of True/False values related to
# when the values in `numbers` ARE equal to 9.
# You should get the answer: [False True False False False False False True False True False False False False False]

print(numbers == 9)


# ********  QUESTION 5  ********
# Filter using the `where()` function to get an array that only includes values of 9. 
# You should get the answer: [9 9 9]

print(numbers[ np.where(numbers == 9) ])


# ********  QUESTION 6  ********
# Filter WITHOUT using the `where()` function to get an array that only includes values of 9.
# You should get the answer: [9 9 9]

print(numbers[ numbers == 9])


# ********  QUESTION 7  ********
# Filter the `numbers` array (you can choose to use where() or to not use where()) to get an array with integers that are
# evenly divisible by 3.
# You should get the answer: [12  9 15  6  9  9]

print(numbers[np.where(numbers % 3 == 0)])
# OR
print(numbers[numbers % 3 == 0])


# ********  QUESTION 8  ********
# Filter the `numbers` array (you can choose to use where() or to not use where()) to get an array with integers that are
# evenly divisible by 4.
# You should get the answer: [12 16 16  8]

print(numbers[np.where(numbers % 4 == 0)])
# OR
print(numbers[numbers % 4 == 0])


# ********  QUESTION 9  ********
# Get a filtered array of `numbers` greater than 5 and less than 11. Print out the array.
# You should get the answer: [ 9  6  9  9 10  8]

print(numbers[(numbers > 5) & (numbers < 11)])


# ********  QUESTION 10  ********
# Get a filtered array of `numbers` less than 5 or greater than 11. Print out the array.
# You should get the answer: [12 15 16  2 16 19  1]

print(numbers[(numbers < 5) | (numbers > 11)])


# ********  QUESTION 11  ********
# Get a filtered array of `numbers` less than 5 and greater than 11. Print out the array.

print(numbers[(numbers < 5) & (numbers > 11)])


# What did this code return?  Why?

''' An empty array was returned. This is because a number cannot simultaneously be less than 5 and greater than 11. '''

# ********  QUESTION 12  ********
# Get a filtered array of `numbers` either not divisible by 3 or are greater than 14.
# You should get the answer: [15 16 11 11  2 10 16 19  1  8]

print(numbers[(numbers % 3 != 0) | (numbers > 14)])


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

filt = numbers_2D > 10
print(filt)


# ********  QUESTION 14  ********
# Why is a matrix of True/False values returned?

''' True indicates where values greater than 10 are located. Because we used a condition on a matrix, a matrix was returned. '''


# ********  QUESTION 15  ********
# Use the `filt` variable as the filter to get an array of numbers from the `numbers_2D` array. 
# (These values should all be greater than 10) This is accomplished by passing in the variable `filt` to the square brackets 
# This looks like `array[ filt ]`.
# Don't worry, working with 2-dimensional arrays is just as easy as working with 1-dimensional arrays!

print(numbers_2D[filt])


# ********  QUESTION 16  ********
# What kind of array got printed out in the previous question (1-dimensional or 2-dimensional)? Why do you think this is?

''' 
A 1-dimensional array was returned. This probably happened because it would be impossible to return a matrix with null spaces. 
We only asked to get all numbers greater than 10 returned, and the easiest way to format them was in an array. 
'''
