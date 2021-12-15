# Name: 
# BTECH #: 

# 1. Use a for loop in combination with the range() function to add together all numbers (5 points)
# between 1 and 100 divisible by 7. Print out the total.

# Your code here


# 2. Use two nested for loops with the range() function to print out a pyramid in the form: (5 points)
# Remember that you can prevent the print function from creating a new line by adding 'end': print("Hello World", end=" ")

# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4
# 0 1 2 3 4 5
# 0 1 2 3 4 5 6

# Your code here


# 3. Guess the number game! (10 points)
# Use the input() function to recieve input from the user on the console on each iteration of the while loop
# to play a number guessing game. In this game, the while loop keeps the program
# running until the user correctly guesses the number (between 1 and 10)
# Don't forget to type cast the input to an integer! >>> int(input("Guess a number: "))

# Create the variable called user_choice before starting the while loop and set it equal to 0. 
# Compare the user_choice to the computer_choice in the while loop condition. 
# If they are equal, then break out of the while loop. If they are not equal, ask for the user's input again.

# We will be importing the random module to generate a random number between 0 and 1
from random import random

computer_choice = int(random() * 10) + 1 # This assigns a random value between 1 and 10 to computer_choice

# Your code here
