# Name:
# BTECH #:

# Import numpy
import numpy as np


# Use the following array to answer the questions below.

numbers = np.array([12, 74, 53, 46, 15, 35, 36, 16, 37, 93, 87, 48, 6, 78, 16, 56, 94, 38, 60, 83, 46, 6])

# Answer the following questions using NumPy functions only. Do not use array methods.

# ********  QUESTION 1  ********
# Find the maximum of the array `numbers` by using the NumPy `amax()` function. Print out the result.

print(np.amax(numbers))


# ********  QUESTION 2  ********
# Find the minimum of the array `numbers` by using the NumPy `amin()` function. Print out the result.

print(np.amin(numbers))


# ********  QUESTION 3  ********
# Find the range of the array `numbers` by using the NumPy `ptp()` function. Print out the result.

print(np.ptp(numbers))


# ********  QUESTION 4  ********
# Find the average of the array `numbers` by using the NumPy `mean()` function. Print out the result.

print(np.mean(numbers))


# ********  QUESTION 5  ********
# Find the median of the array `numbers` by using the NumPy `median()` function. Print out the result.

print(np.median(numbers))


# ********  QUESTION 6  ********
# Find the sum of the array `numbers` by using the NumPy `sum()` function. Print out the result.

print(np.sum(numbers))


# ********  QUESTION 7  ********
# Find the standard deviation of the array `numbers` by using the NumPy `std()` function. Print out the result.

print(np.std(numbers))


# ********  QUESTION 8  ********
# Find the first and third quartiles of the array `numbers` by using the NumPy `quantile()` function. Print 
# out the result.

print(np.quantile(numbers, .25))
print(np.quantile(numbers, .75))


# -------------------------------------------------------------------------------------------------------

# Answer the following questions using array methods only. Do not use NumPy functions.

# ********  QUESTION 9  ********
# Find the maximum of the array `numbers` by using the `.max()` method on the array. Print out the result.

print(numbers.max())


# ********  QUESTION 10  ********
# Find the minimum of the array `numbers` by using the `.min()` method on the array. Print out the result.

print(numbers.min())


# ********  QUESTION 11  ********
# Find the range of the array `numbers` by using the `.ptp()` method on the array. Print out the result.

print(numbers.ptp())


# ********  QUESTION 12  ********
# Find the average of the array `numbers` by using the `.mean()` method on the array. Print out the result.

print(numbers.mean())


# ********  QUESTION 13  ********
# Find the sum of the array `numbers` by using the `.sum()` method on the array. Print out the result.

print(numbers.sum())


# ********  QUESTION 14  ********
# Find the standard deviation of the array `numbers` by using the `.std()` method on the array. Print out the result.

print(numbers.std())


# ********  QUESTION 15  ********
# One of the aggregate functions that we used as a NumPy function we did not use as an array method. This is because
# it is not available as an array method. Which aggregate function was this?

''' Median is not an aggregate function that can be used as an array method. '''


# ********  QUESTION 16  ********
# Create a function called "isRightSkewed" that returns True if the data set is right skewed, and False
# if the data set is left skewed or not skewed at all. Remember that right skewness occurs when the mean
# is greater than the median.
def isRightSkewed(array):
    if np.mean(array) > np.median(array):
        return True
    else:
        return False
