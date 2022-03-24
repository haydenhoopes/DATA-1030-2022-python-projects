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


# -------------------------------------------------------------------------------------------------------

# Answer the following questions using array methods only. Do not use NumPy functions.

# ********  QUESTION 8  ********
# Find the maximum of the array `numbers` by using the `.max()` method on the array. Print out the result.

print(numbers.max())


# ********  QUESTION 9  ********
# Find the minimum of the array `numbers` by using the `.min()` method on the array. Print out the result.

print(numbers.min())


# ********  QUESTION 10  ********
# Find the range of the array `numbers` by using the `.ptp()` method on the array. Print out the result.

print(numbers.ptp())


# ********  QUESTION 11  ********
# Find the average of the array `numbers` by using the `.mean()` method on the array. Print out the result.

print(numbers.mean())


# ********  QUESTION 12  ********
# Find the sum of the array `numbers` by using the `.sum()` method on the array. Print out the result.

print(numbers.sum())


# ********  QUESTION 13  ********
# Find the standard deviation of the array `numbers` by using the `.std()` method on the array. Print out the result.

print(numbers.std())


# ********  QUESTION 14  ********
# One of the aggregate functions that we used as a NumPy function we did not use as an array method. This is because
# it is not available as an array method. Which aggregate function was this?

''' Median is not an aggregate function that can be used as an array method. '''



# ********  QUESTION 15  ********
# Create a function called "isRightSkewed" that returns True if the data set is right skewed, and False
# if the data set is left skewed or not skewed at all. Remember that right skewness occurs when the mean
# is greater than the median.
def isRightSkewed(array):
    if np.mean(array) > np.median(array):
        return True
    else:
        return False



# ********  QUESTION 2  *********
# Create a function that accepts a matrix of data. The first columns are the actual values that we are
# interested in and the second column are the weights. With this information, the function will compute the
# weighted average of the data in the first column. Below is an example of how the matrix will look.

matrix = np.array([
    [50, .1],
    [100, .2],
    [150, .3],
    [200, .4]
])

def weightedAverage(matrix):
    return np.average(matrix[:, 0], weights=matrix[:, 1])



# ********  QUESTION 3  ********
# Imagine that you have a dataset where each row represents a different pizza restaurant and each column 
# represents sales for a given day of the week. The first column is the id of the restaurant. 
# The data set looks like the following:

pizza_sales = np.array([
    [ 1, 357, 407, 357, 387, 581, 240, 398],
    [ 2, 527, 593, 587, 617, 682, 667, 589],
    [ 3, 106, 693, 163, 852, 330, 683, 631],
    [ 4, 93, 84, 93, 98, 99, 88, 91],
    [ 5, 534, 226, 193, 584, 165, 565, 205],
    [ 6, 952, 751, 675, 653, 550, 730, 601],
    [ 7, 366, 233, 217, 247, 590, 520, 257]
])

# With this matrix, create a function that computes the standard deviation of the average weekly sales 
# among all the pizza restaurants. The first column ("id") should not be included in the calculations.
def stDevOfAveragePizzaSales(table):
    averageSales = []
    for restaurant in table:
        averageSales.append(np.mean(restaurant[1:]))
    return np.std(np.array(averageSales))
