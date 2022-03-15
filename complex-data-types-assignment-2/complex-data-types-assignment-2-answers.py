# Name: 
# BTECH #: 


# 1. Use an if statement that determines whether the following numbers are odd or even. Print out
#    a message stating either "It is even" or "It is odd". Remember that you can use the modulus
#    operator  %  to get the remainder after dividing. Thus, 4 % 2 is 0 and 5 % 2 is 1. If % 2
#    equals 0, the number is even. If it equals 1, the number is odd. Use the same if statement
#    each time.

number_1 = 3
if number_1 % 2 == 1:
    print("It is odd")
else:
    print("It is even")


number_2 = 4
if number_2 % 2 == 1:
    print("It is odd")
else:
    print("It is even")


number_3 = 55564673
if number_3 % 2 == 1:
    print("It is odd")
else:
    print("It is even")


# 2. Use if statements to determine if the following numbers are greater than, less than, or equal to 0. Use
#    separate if-elif-else statments for each. If the number is greater than 0, print a
#    message that says "Greater than 0". If the number is less than 0, print out "Less than 0".
#    Otherwise, print out "Equal to 0". Use the same if statement each time.

number_1 = 365
if number_1 > 0:
    print("Greater than 0")
elif number_1 < 0:
    print("Less than 0")
else:
    print("Equals 0")


number_2 = -50
if number_2 > 0:
    print("Greater than 0")
elif number_2 < 0:
    print("Less than 0")
else:
    print("Equals 0")


number_3 = 0
if number_3 > 0:
    print("Greater than 0")
elif number_3 < 0:
    print("Less than 0")
else:
    print("Equals 0")


# 3. According to the Chinese zodiac calendar, each year is attributed to a certain animal. The order of the
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

if (year-1900) % 12 == 0:
    print("Rat")
elif (year-1900) % 12 == 1:
    print("Ox")
elif (year-1900) % 12 == 2:
    print("Tiger")
elif (year-1900) % 12 == 3:
    print("Rabbit")
elif (year-1900) % 12 == 4:
    print("Dragon")
elif (year-1900) % 12 == 5:
    print("Snake")
elif (year-1900) % 12 == 6:
    print("Horse")
elif (year-1900) % 12 == 7:
    print("Sheep")
elif (year-1900) % 12 == 8:
    print("Monkey")
elif (year-1900) % 12 == 9:
    print("Rooster")
elif (year-1900) % 12 == 10:
    print("Dog")
else:
    print("Pig")


# 4. Create if statements that test the following conditions on the numbers 3.14 and 100. Use the key words and/or and 
#    comparison operators (>, >=, ==, !=, <, <=) appropriately.
#    a. If 3.14 is greater than 0 and 3.14 is less than 10, print out "It's between 0 and 10".
#    b. If 100 is less than -60 or greater than 0, print out "It's either less than -60 or greater than 0".
#    c. If (100 is greater than 10 and 3.14 is less than 50) and 100 does not equal 73, print out "I think I'm doing something right".

#    a.
if 3.14 > 0 and 3.14 < 10:
    print("It's between 0 and 10")

#    b.
if 100 < -60 or 100 > 0:
    print("It's either less than -60 or greater than 0")

#    c.
if (100 > 10 and 3.14 < 50) or 100 != 73:
    print("I think I'm doing something right")


# 5. Use a for loop to print out each letter in the following phrase:
phrase = "Yankee doodle came to town"

# Your code here


# 6. Create a list of integers that represent ages of people in your family (you can make it up). Give the list at least 3 integers. 
#    Use a for-loop to print out each person's age one year from now (print the age plus 1).

# Your code here


# 7. Use a for-loop to print out all numbers between 5 and 10.

# Your code here


# 8. Use a for loop in combination with the range() function to add together all numbers (5 points)
# between 1 and 100 divisible by 7. Print out the resulting total.

# Your code here
total = 0
for i in range(1,100):
    if i % 7 == 0:
        total += i
print(total)


# 9. Create a variable called total and set it equal to 0. Then, use a while loop to add 5 to the total until the total is
#    greater than 100.

# Your code here


# 10. Guess the number game! (10 points)
# Use the input() function to recieve input from the user on the console on each iteration of the while loop
# to play a number guessing game. In this game, the while loop keeps the program
# running until the user correctly guesses the number (between 1 and 10)
# Don't forget to type cast the input to an integer! >>> int(input("Guess a number: "))

# Hint: Create a variable called "playing" and set it to True. Then start the while loop by stating
# while playing. Set playing to False when the user guesses correctly to end the while loop.

# We will be importing the random module to generate a random number between 0 and 1
from random import random

computer_choice = int(random() * 10) + 1 # This assigns a random value between 1 and 10 to computer_choice

playing = True # while playing is True, keep playing the game. When the user guesses correctly, this should become False

# Your code here

while playing:
    user_choice = int(input("Guess a number between 1 and 10: "))
    if user_choice == computer_choice:
        playing = False
        print("You win!")
    else:
        print("That's not it.")