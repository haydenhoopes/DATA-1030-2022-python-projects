# Name:
# BTECH #:

# In this assignment, you will become more familiar with functions and how to 
# create and use them in Python.


print("********  QUESTION 1  ********")

def add_three_numbers(a, b, c=3):
    return a + b + c


# Referencing the function `add_two_numbers()` from above, answer the following 
# questions:

# Ex. What is the function name?
# Answer: add_three_numbers

# Question 1a: How many parameters does the function have?
# Answer: Three

# Question 1b: How many default parameters does the function have?
# Answer: One

# Question 1c: How many required parameters does the function have?
# Answer: Two

# Question 1d: Does the function return anything?
# Answer: Yes

# Question 1e: What data type would you expect the function to return?
# Answer: A number, either of float or an integer

# Question 1f: Without adding any code, will the function print anything out? 
# Why or why not?
# Answer: No, the print function isn't used


print("********  QUESTION 2  ********")

# Referencing the function `add_three_numbers()` from above, call the function
# `add_three_numbers()` by passing two or three numbers into it. Run this Python
# file and scroll through your Command Prompt and look under the heading for 
# question 2. You should not see any output.

add_three_numbers(3, 5, 2)


print("********  QUESTION 3  ********")

# Referencing the function `add_three_numbers()` from above, call the function 
# `add_three_numbers()` by passing two or three numbers into it. Save the output
# into a variable and print out the variable. You should see the sum of the
# numbers printed out when your run the file underneath the Question 3 header.

results = add_three_numbers(3, 5, 2)
print(results)


print("********  QUESTION 4  ********")

# When dealing with functions, what is the difference between using the 
# `print()` function and the `return` key word? In which circumstances would you
# use one or the other?

'''
    Print just shows the value on the screen, but return passes it back to 
    whatever called it to be used more in the code.
'''


print("********  QUESTION 5  ********")

# Create a function that prints out "I <3 Python!" when it is called. Then, call
# it. You should see the text appear in your Command Prompt after running the 
# file.

def i_heart_python():
    print("I <3 Python!")

i_heart_python()


print("********  QUESTION 6  ********")

# Create a function that prints out "Hello, user" when it is called without a
# parameter and "Hello, John" when called with parameter called `name` set to 
# "John". Then, call the function once without passing in any parameters, a 
# second time passing in the name "John", and a third time by passing in your 
# own name.

# In other words, the function should have a single parameter `name` that has a
# default value of `user`.

def hello(name="user"):
    print("Hello, " + name)

hello()
hello("John")
hello("Hayden")

print("********  QUESTION 7  ********")

# Recall that the formula for finding the slope of a line is `y = mx + b` where
# `x` and `y` are points on a graph, `b` is the y-intercept, and `m` is the 
# slope of the line. We can rearrange this formula to calculate the slope of any
# given line as `m = (y - b) / x`. Below, you will be given `x`, `y`, and `b`
# and should create a function to calculate `m`.

# Create a function called `find_slope()` that takes in parameters `x`, `y`, and
# `b` and uses them to calculate the slope of a line `m`. Return the slope but
# DO NOT print it inside of the function body.

# After creating the function, call it once by passing in parameters x=1, y=4,
# and b=3 and print out the results. You should see an ouput of 1.0.

def find_slope(x, y, b):
    return (y - b) / x

print(find_slope(1, 4, 3))


print("********  QUESTION 8  ********")

def get_area(radius):
    pi = 3.1415
    area = pi * (radius ** 2)

# Observe the function `get_area()` above. Why doesn't calling this function 
# below print anything out, even after the `print()` function is used? (Note: 
# The word "None" is printed out). How would you change this function (without 
# adding the `print()` function to it) to make the area be printed out 
# correctly?

print(get_area(10))

'''
    The area needs to be returned out of the function.
'''


print("********  QUESTION 9  ********")

# Create a new function called `get_circumference()` that accepts the radius of 
# a circle as a parameter. To then calculate the circumference, use the formula:
# circumference = 2 * pi * radius. You can use 3.1415 instead of pi.

# Do not use the `print()` function inside of the function body. Instead, make
# sure to `return` the circumference at the end of the function body. Then, call
# the function and print out its results three times with a different radius 
# each time.

def get_circumference(radius):
    pi = 3.1415
    circumference = 2 * pi * radius
    return circumference

print(get_circumference(10))
print(get_circumference(20))
print(get_circumference(30))


print("********  QUESTION 10 ********")

# The code below includes a function that is meant to be able to calculate a 
# person's age given their birth year and an end year. In this way, a person 
# born in 1993 could calculate how old they were in 2020.

# Something is wrong with this code that does not let it run correctly. What is 
# wrong with the function `get_age()`?

# Hint: Run the Python file and look at the output to see what happens.

birth_year = 1993
current_year = 2020

def get_age(start_year, end_year):
    age = current_year - birth_year
    return age

print(get_age(1985, 2022)) # Born in 1985
print(get_age(1968, 2025)) # Born in 1968
print(get_age(1130, 1203)) # Born in Medieval Times, 1130


'''
    The function is referencing variables from outside of the function, but 
    should instead reference the function parameters.
'''


print("********  QUESTION 11 ********")

# Fix the function `get_age()` from above so that it prints out the correct age.

birth_year = 1993
current_year = 2020

def get_age(start_year, end_year):
    age = current_year - birth_year
    return age

print(get_age(1985, 2022)) # Born in 1985
print(get_age(1968, 2025)) # Born in 1968
print(get_age(1130, 1203)) # Born in Medieval Times, 1130



print("********  QUESTION 12 ********")

def add_exclamation(word):
    print(word + "!!!")
    add_exclamation(word)

# add_exclamation('wut')

# Observe the function `add_exclamation()` from above that adds exclamation
# points to a given word, which is provided as a parameter. This function calls
# itself again inside of its function body. What is going to happen when this 
# function is called? Why will it happen?

# Hint: Try calling the function by passing in a word to see what happens. What
# kind of error do you get? 

'''
    The function shouldn't call itself. Since it does this, it's going to print
    the word a whole bunch of times until Python runs out of memory.
'''


print("********  QUESTION 13 ********")

def multiply_numbers(a, b):
    product = a * b
    return product

# print(product) # UNCOMMENT ME!

# Observe the function above called `multiply_numbers()` which takes two numbers
# and multiplies them together. Notice below the function that a line of code
# has been commented out that prints out the `product` variable from the 
# `multiply_numbers()` function.

# Uncomment that line of code and notice that an error ocurrs when you try to 
# run the file. Why does this line of code cause an error?

'''
    Product is a variable that is only available inside of the function, not
    outside of it.
'''


print("********  QUESTION 14 ********")

# Create a function called `solve_world_hunger()` that solves the international
# hunger crisis. Well, since you probably don't know all of the things that your
# function needs to do to solve such a problem quite yet, just create the 
# function and put in the word `pass` to temporarily fill in the function and 
# tell it to do nothing when run. Then, run it.

def solve_world_hunger():
    pass


print("********  QUESTION 15 ********")

# Create four functions called `add()`, `subtract()`, `multiply()` and 
# `divide()`. Each of these functions should accept two parameters representing
# two numbers, and each should return the sum, difference, product, and 
# dividend, respectively. Call each function once after creating it and print 
# out the results.

def add(a, b):
    return a + b

print(add(4, 2))

def subtract(a, b):
    return a - b

print(subtract(4, 2))

def multiply(a, b):
    return a * b

print(multiply(4, 2))

def divide(a, b):
    return a / b

print(divide(4, 2))


print("********  QUESTION 16 ********")

# Create a function called `perform_operations()` that accepts two numbers. The
# function should create four variables using these two numbers called `sum`, 
# `difference`, `product`, and `dividend` which are created by calling each of 
# the four functions created previously (ie. `add()`, `subtract()`, 
# `multiply()`, and `divide()`). The results of each operation should also be
# printed out.

# Then, call your function `perform_operations()` once, passing in the numbers 
# 9 and 3. You should see printed out the numbers 12, 6, 27, and 3.

def perform_operations(a, b):
    print(add(a, b))
    print(subtract(a, b))
    print(multiply(a, b))
    print(divide(a, b))

perform_operations(9, 3)