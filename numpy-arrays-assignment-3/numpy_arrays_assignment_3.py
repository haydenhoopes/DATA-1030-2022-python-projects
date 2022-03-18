# Name:
# BTECH #:

# Import the NumPy library here
# Your code here


# Use the array below in the following questions.
numbers = np.array([12, 9, 15, 16, 11, 6, 11, 9, 2, 9, 10, 16, 19, 1, 8, 10, 13, 4, 11, 5])


# ********  QUESTION 1  ********
# Use the `where()` function to get an array of indexes that correspond to the location of each number 11 in the
# `numbers` array. Print out this array.

# Your code here


# ********  QUESTION 2  ********
# Use the `where()` function to get an array of indexes that correspond to the locations of numbers less than 6.

# Your code here


# ********  QUESTION 3  ********
# Use the `where()` function to get an array of indexes that correspond to the locations of numbers greater than 15.

# Your code here


# ********  QUESTION 4  ********
# Use the `where()` function to get an array of indexes that correspond to the locations of numbers evenly divisible
# by 3.

# Your code here


# ********  QUESTION 5  ********
# Notice that in each of the arrays printed above, the numbers printed do not all correspond to the condition (ie.
# getting numbers equal to 11 returns 4, which is not equal to 11). Why did this happen?

''' Your answer here. '''


# ********  QUESTION 6  ********
# Pass a `where()` function into the `numbers` array inside square brackets to filter it down to values evenly divisible
# by 3. Print out the filtered array.

# Your code here


# ********  QUESTION 7  ********
# Get a filtered version of the array `numbers` WITHOUT passing in the `where()` function. Instead, pass in a simple
# comparison in the format array[ array == # ]. Filter to numbers evenly divisible by 4.

# Your code here


# ********  QUESTION 8  ********
# Get a filtered array of `numbers` greater than 5 and less than 11. Print out the array.

# Your code here


# ********  QUESTION 9  ********
# Get a filtered array of `numbers` less than 5 or greater than 11. Print out the array.

# Your code here


# ********  QUESTION 10  ********
# Get a filtered array of `numbers` either not divisible by 3 or are greater than 14.

# Your code here


# Use the following 2-dimensional array to answer the questions below.
numbers_2D = [[16, 16,  6,  1,  4],
              [15, 10,  7, 15, 14],
              [ 5, 15,  7,  6, 17],
              [ 8,  4,  2,  2,  2],
              [ 3, 15,  4, 12,  1]]


# ********  QUESTION 11  ********
# Create a filter that looks for items in the `numbers_2D` array greater than 10 and save it to a variable.
# It should look something like `filt = a > #`. Print out the filt variable.

# Your code here


# ********  QUESTION 12  ********
# What did the `filt` variable created previously look like? What data types did it have?

''' Your answer here. '''


# ********  QUESTION 13  ********
# Use the `filt` variable as the filter to get an array of numbers from the `numbers_2D` array greater than 10. In
# other words, pass in the variable `filt` to the square brackets instead of typing the filter out `array[ filt ]`.
# Don't worry, working with 2-dimensional arrays is just as easy as working with 1-dimensional arrays!

# Your code here


# ********  QUESTION 14  ********
# What kind of array got printed out in the previous question (1-dimensional or 2-dimensional)?

''' Your answer here. '''
