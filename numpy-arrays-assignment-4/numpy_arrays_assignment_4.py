# Name:
# BTECH #:

# Import numpy
# Your code here


# ********  QUESTION 1  ********
# Create a function called "isRightSkewed" that returns True if the data set is right skewed, and False
# if the data set is left skewed or not skewed at all. Remember that right skewness occurs when the mean
# is greater than the median.
def isRightSkewed(array):
    # Your code here
    return



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
    # Your code here
    return



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
    # Your code here
    return
