# Name:
# BTECH #:

# You should import the NumPy library here
# Your code here


# You hadn't worked for Apple for very long before the CEO looked to you, the company's data analyst,
# for answers. The new iPhones haven't been selling as much as they used to, but the company also
# recently increased its price point so that more revenue was generated per sale than before. The CEO
# has given you data on iPhone sales for the past twelve months as a list and wants you to 
# answer the following questions:

iphone_sales = [215.05, 190.26, 169.22, 231.22, 211.88, 216.76, 217.72, 220.48, 215.76, 202.31, 230.1, 250.87]

# *********  QUESTION 1  *********
# First, convert the list of iPhone sales to a NumPy array.

# Your code here


# *********  QUESTION 2  *********
# What is the range of sales over the past twelve months? Print this figure out.

# Your code here


# *********  QUESTION 3  *********
# What have been the average sales over the past twelve months? Print this figure out.

# Your code here


# *********  QUESTION 4  *********
# What has been the average sales during the past three months? Print this figure out.

# Your code here


# *********  QUESTION 5  *********
# Comparing the average sales for the past twelve months to the average sales in the past three months,
# are average sales in the past three months greater than or less than the twelve month average?
# What might this say about the movement of of the company sales? Are they increasing on average or
# decreasing?

''' 
    Your answer here.
'''


# -----------------------------------------------------------------------------------------------------

# Imagine that you are the owner of Bob's Burritos, a food truck that started selling food just four
# weeks ago in the Bridgerland parking lot. You have been recording sales since you opened and now have
# four complete weeks of sales data. The food truck is open every day of the week (meaning you have
# 28 records of sales).

# *********  QUESTION 6  *********
# Create a NumPy array with 7 columns and 4 rows where each column represents a day
# of the week and each each row represents a week. Make up sales data that you would
# expect from a burrito truck.

# Your code here


# *********  QUESTION 7  *********
# According to the data in the `burrito_sales` array, what is the average sales on the last day of the week?
# Print out the answer.

# Your code here


# *********  QUESTION 8  *********
# According to the data in the `burrito_sales` array, what was the amount of the 
# highest selling day during the first month of business? Use the `np.amax()` 
# function or the `.max()` method. Print out the answer.

# Your code here


# *********  QUESTION 9  *********
# Print out an array of True/False values from the `burrito_sales` array where True indicates a day whose sales
# were higher than the overall average sales.

# Your code here


# *********  QUESTION 10  *********
# The burrito maker, Bob, wants to create a promotion to entice people to eat more burritos on slow days.
# According to the data, which day of the week has the least average sales? Assume that the first column is
# Sunday.

# Your code here

''' Your answer here. '''


# *********  QUESTION 11  *********
# The cashier (also named Bob) accidentally included sales tax recieved from clients on the sales amounts from 
# the first week. Replace all the values in the first row with the same amount divided by 1.05 (assuming sales 
# tax is 5%). Print out the new `burrito_sales` array.

# Your code here


# *********  QUESTION 12  *********
# What is the standard deviation of `burrito_sales`? Save the standard deviation as a variable and print it out.

# Your code here


# *********  QUESTION 13  *********
# The restaurant's accountant (Bob) wants to know how many days had sales amounts that were outliers.
# Assuming that an outlier is anything greater than the Inner Quartile Range (IQR) multiplied by 1.5, are there 
# any outliers? How many are there? Get back an array of values greater than 1.5 times the IQR and print out its
# length. You can get 1.5 times the IQR by using the quantile function:
#   (np.quantile(array, .75) - np.quantile(array, .25)) * 1.5.
#   - Print out 1.5 times the IQR
#   - Print out the number of items that are outliers.
# Any number greater than this number would be considered an outlier.

# Your code here
