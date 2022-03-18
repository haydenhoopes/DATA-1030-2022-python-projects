# Name: 
# BTECH #: 


# 1. Use an if statement that determines whether the following numbers are odd or even. Print out
#    a message stating either "It is even" or "It is odd". Remember that you can use the modulus
#    operator  %  to get the remainder after dividing. Thus, 4 % 2 is 0 and 5 % 2 is 1. If % 2
#    equals 0, the number is even. If it equals 1, the number is odd. Use the same if statement
#    each time.

number_1 = 3
# Your code here


number_2 = 4
# Your code here


number_3 = 55564673
# Your code here


# 2. Turn the if statements you made above into a function that takes a single integer as a parameter. The
#    function should pass the integer into the if statement, which determines if it is even or odd. Call the function
#    three times with different numbers.

# Your code here


# 3. Use if statements to determine if the following numbers are greater than, less than, or equal to 0. Use
#    separate if-elif-else statments for each. If the number is greater than 0, print a
#    message that says "Greater than 0". If the number is less than 0, print out "Less than 0".
#    Otherwise, print out "Equal to 0". Use the same if statement each time.

number_1 = 365
# Your code here


number_2 = -50
# Your code here


number_3 = 0
# Your code here


# 4. Turn the if statements you just made into a single function that takes an integer as a parameter. The function
#    should pass the integer into the if statement, which determines if it is greater than, less than, or equal
#    to 0. Call the function three times.

# Your code here


# 5. According to the Chinese zodiac calendar, each year is attributed to a certain animal. The order of the
#    zodiac signs are as follows:
#    - (1900) Rat       0
#    - (1901) Ox        1
#    - (1902) Tiger     2
#    - (1903) Rabbit    3
#    - (1904) Dragon    4
#    - (1905) Snake     5
#    - (1906) Horse     6
#    - (1907) Sheep     7
#    - (1908) Monkey    8
#    - (1909) Rooster   9
#    - (1910) Dog       10
#    - (1911) Pig       11
#    The zodiac sign for any given year can be calculated by subtracted 1900 from the year and then getting its
#    remainder when divided by 12. For example, the year 2022 would be the year of the tiger because
#    2022 - 1900 = 122 and 122 % 12 = 2. The number 2 (as seen above) corresponds to the tiger.
#    Create a long if-elif-else function that prints out the zodiac sign depending on the year given. Choose
#    any year that you want.

year = 2022

# Your code here


# 6. Create if statements that test the following conditions on the numbers 3.14 and 100. Use the key words and/or and 
#    comparison operators (>, >=, ==, !=, <, <=) appropriately.
#    a. If 3.14 is greater than 0 and 3.14 is less than 10, print out "It's between 0 and 10".
#    b. If 100 is less than -60 or greater than 0, print out "It's either less than -60 or greater than 0".
#    c. If (100 is greater than 10 and 3.14 is less than 50) and 100 does not equal 73, print out "I think I'm doing something right".

#    a.
# Your code here

#    b.
# Your code here

#    c.
# Your code here


# 7. Use a for loop to print out each letter in the following phrase:
phrase = "Yankee doodle came to town"

# Your code here


# 8. Create a list of integers that represent ages of people in your family (you can make it up). Give the list at least 3 integers. 
#    Use a for-loop to print out each person's age one year from now (print the age plus 1).

# Your code here


# 9. Use a for-loop and the range() function to print out all numbers between 5 and 10. Make sure that 10 is printed as well! You may need to use 11
#    as then end parameter in the range function since it is not inclusive (doesn't include last number).

# Your code here


# 10. Use a for loop in combination with the range() function to add together all numbers (5 points)
# between 1 and 100 divisible by 7. Print out the resulting total.

# Your code here


# 11. Create a variable called total and set it equal to 0. Then, use a while loop to add 5 to the total until the total is
#    greater than 100. Print out the total when you finish.

# Your code here


# 12. Guess the number game! (10 points)
# Use the input() function to recieve input from the user on the console on each iteration of the while loop
# to play a number guessing game. In this game, the while loop keeps the program
# running until the user correctly guesses the number (between 1 and 10)
# Don't forget to type cast the input to an integer! >>> int(input("Guess a number: "))

# Hint: Create a variable called "playing" and set it to True. Then start the while loop by stating
# while playing. Set playing to False when the user guesses correctly to end the while loop.

# We will be importing the random module to generate a random number between 0 and 1
from random import random

computer_choice = int(random() * 10) + 1 # This assigns a random value between 1 and 10 to computer_choice

# Your code here
