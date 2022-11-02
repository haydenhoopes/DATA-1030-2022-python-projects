# Name:
# BTECH #:

# You should import the NumPy library here
import numpy as np


# You hadn't worked for Apple for very long before the CEO looked to you, the company's data analyst,
# for answers. The new iPhones haven't been selling as much as they used to, but the company also
# recently increased its price point so that more revenue was generated per sale than before. The CEO
# has given you data on iPhone sales for the past twelve months as a list and wants you to 
# answer the following questions:

iphone_sales = [215.05, 190.26, 169.22, 231.22, 211.88, 216.76, 217.72, 220.48, 215.76, 202.31, 230.1, 250.87]

# *********  QUESTION 1  *********
# First, convert the list of iPhone sales to a NumPy array.

iphone_sales = np.array(iphone_sales)


# *********  QUESTION 2  *********
# What is the range of sales over the past twelve months? Print this figure out.

print(iphone_sales.ptp())


# *********  QUESTION 3  *********
# What have been the average sales over the past twelve months? Print this figure out.

print(np.mean(iphone_sales))


# *********  QUESTION 4  *********
# What has been the average sales during the past three months? Print this figure out.

print(np.mean(iphone_sales[9:]))


# *********  QUESTION 5  *********
# Comparing the average sales for the past twelve months to the average sales in the past three months,
# are average sales in the past three months greater than or less than the twelve month average?
# What might this say about the movement of of the company sales? Are they increasing on average or
# decreasing?

''' 
    Average sales in the past three months are sligtly greater than total sales in the past twelve months.
    This seems to indicate that average sales are going up.
'''


# -----------------------------------------------------------------------------------------------------

# Imagine that you are the owner of Bob's Burritos, a food truck that started selling food just four
# weeks ago in the Bridgerland parking lot. You have been recording sales since you opened and now have
# four complete weeks of sales data. The food truck is open every day of the week (meaning you have
# 28 records of sales).

# *********  QUESTION 6  *********
# Create a NumPy array with 7 columns and 4 rows where each column represents a day of the week and each
# each row represents a week. Make up sales data that you would expect from a burrito truck.

burrito_sales = np.array([
    [33, 30, 83, 52, 92, 0, 54], 
    [44, 43, 17, 30, 59, 19, 62], 
    [41, 4, 72, 13, 60, 31, 78], 
    [9, 40, 68, 69, 107, 26, 132]
])

# *********  QUESTION 7  *********
# According to the data in the `burrito_sales` array, what is the average sales on the last day of the week?
# Print out the answer.

print(burrito_sales[:,-1].mean())


# *********  QUESTION 8  *********
# According to the data in the `burrito_sales` array, what was the amount of the highest selling day during
# the first month of business? Print out the answer.

print(burrito_sales.max())


# *********  QUESTION 9  *********
# Print out an array of True/False values from the `burrito_sales` array where True indicates a day whose sales
# were higher than the overall average sales.

overall_average = burrito_sales.mean()

print(burrito_sales > overall_average)


# *********  QUESTION 10  *********
# The burrito maker, Bob, wants to create a promotion to entice people to eat more burritos on slow days.
# According to the data, which day of the week has the least average sales? Assume that the first column is
# Sunday.

print(f"Sunday average sales: ${burrito_sales[:,0].mean()}")
print(f"Monday average sales: ${burrito_sales[:,1].mean()}")
print(f"Tuesday average sales: ${burrito_sales[:,2].mean()}")
print(f"Wednesday average sales: ${burrito_sales[:,3].mean()}")
print(f"Thursday average sales: ${burrito_sales[:,4].mean()}")
print(f"Friday average sales: ${burrito_sales[:,5].mean()}")
print(f"Saturday average sales: ${burrito_sales[:,6].mean()}")

''' Friday has the least average sales. '''


# *********  QUESTION 11  *********
# The cashier (also named Bob) accidentally included sales tax recieved from clients on the sales amounts from 
# the first week. Replace all the values in the first row with the same amount divided by 1.05 (assuming sales 
# tax is 5%). Print out the new `burrito_sales` array.

burrito_sales[0,:] = burrito_sales[0,:] / 1.05
print(burrito_sales)


# *********  QUESTION 12  *********
# What is the standard deviation of `burrito_sales`? Save the standard deviation as a variable and print it out.

sd = burrito_sales.std()
print(sd)


# *********  QUESTION 13  *********
# The restaurant's accountant (Bob) wants to know how many days had sales amounts 
# that were outliers. Use the function `get_burrito_sales_outliers()` below to 
# RETURN an array of burrito sales that are outliers. Then, print out the results of
# the function. You should add a single line of code inside of the function and a
# single line of code after the function to test it.

# Be sure to uncomment the lines of code that say # UNCOMMENT ME at the end.

# Outliers are values that are far away from the average. We can check if a value is
# an outlier by using the function below:

def get_burrito_sales_outliers(array):
    # The Inner-Quartile Range is the 75th percentile minus the 25th percentile.
    iqr = np.quantile(burrito_sales, .75) - np.quantile(burrito_sales, .25)

    # We multiply the IQR by 1.5 and then add the resulting number onto the value
    # located at the 75th percentile called `upper_threshold`. Any number greater
    # than the upper threshold is considered an outlier.
    upper_threshold = np.quantile(burrito_sales, .75) + (iqr * 1.5)

    # Use NumPy to return an array of burrito sales greater than `upper_threshold`.
    # Remember that because you are inside of a function, you should use the local
    # variable `array` instead of `burrito_sales`.
    return array[array > upper_threshold]

get_burrito_sales_outliers(burrito_sales)
