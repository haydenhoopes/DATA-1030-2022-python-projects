# This is a review of frequently missed questions

# ********  Complex Data Types Assignment 1  ********
# 10. Using the following list of numbers:
#    a. Use the len() and sum() functions to compute the mean of the set of numbers.
#       Remember that mean can be computed as sum / length of list (number of 
#       observations)
#    b. Get the median value. Remember that median is the middle value of a sorted 
#       list, computed as the nth value in the list where n is len() // 2 (integer 
#       division).
#
#       Hint: The length of the list is 37. That means that if you divide by 2 (to 
#       get the position of the middle number), you will get 18.5. Unfortunately, 
#       you can't use a decimal number as an index! Furthermore, the number 19 will 
#       actually return the number in position 18 (since the first item is 0, then 1, 
#       etc.).
#
#       By using floor division (//) we can automatically get 18.5 and round it down, 
#       getting the correct index for item 19 (the middle number).
#    c. Print out the mean and median. (The mean is 21, the median is 7)

numbers = [5,5,8,2,9,1,100,34,2,33,7,7,7,3,1,6,60,76,6,2,9,85,3,8,5,23,0,3,69,35,50,3,3,86,1,1,45]


# ********  Complex Data Types Assignment 2  ********
# 12. Guess the number game!
# Use the input() function to recieve input from the user on the console on each 
# iteration of the while loop to play a number guessing game. In this game, the 
# while loop keeps the program running until the user correctly guesses the number 
# (between 1 and 10). 
# Don't forget to type cast the input to an integer! int(input("Guess a number: "))

# Hint: Create a variable called "playing" and set it to True. Then start the while 
# loop by stating `while playing`. Set playing to False when the user guesses 
# correctly to end the while loop.

# We will be importing the random module to generate a random number between 0 and 1
from random import random

computer_choice = int(random() * 10) + 1 # This assigns a random value between 1 and 10 to computer_choice

playing = True # while playing is True, keep playing the game. When the user guesses correctly, this should become False

while playing:
    user_choice = int(input("Guess a number between 1 and 10: "))
    if user_choice == computer_choice:
        playing = False
        print("You win!")
    else:
        print("That's not it.")


# ********  Complex Data Types Project  ********
# 9. You want to build a game that finds how long it takes for you to collect all of 
#    the face cards in a deck of cards. For our purposes, we will use only one suit 
#    of cards numbered 2-14 where 11 = "Jack", 12 = "Queen", 13 = "King", and 14 = "Ace"
    # If you are to pick up cards one at a time from your deck, we want to know how many cards you need to pick before you have all the face cards
    # Below, we have included code that generates a randomized list of the deck of cards 2-14.

import random
possibilities = [x for x in range(2,15)]
random.shuffle(possibilities)

        # Create an empty list called cards_picked
        # Start a while loop that runs as long as the length of cards_picked is less than 13
        # Add the first card that appears in possibilities to cards_picked
        # Now remove the first card from possibilities
        # Outside of your while loop, print(cards_picked)
            # Test your code. You should see a randomized list of the cards 2-14

cards_picked = []
while len(cards_picked) < 13:
    picked = possibilities[0]
    cards_picked.append(picked)
    if 11 in cards_picked and 12 in cards_picked and 13 in cards_picked and 14 in cards_picked: # added in 10
        break # added in 10
    possibilities.pop(0)
# print(cards_picked)
print(f"Number of picks: {len(cards_picked)}") # added in 10

# 10. Add to your while loop in Question 9. 
    # Add an if statement after you remove the first card from possibilities
    # The if statement should instruct the code to break if cards 11 and 12 and 13 and 14 are in your hand (cards_picked)
    # Change the print statement outside of the for loop to print "Number of picks: #" where number represents the number of cards in your hand.
 