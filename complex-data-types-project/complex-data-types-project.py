# Name: 
# BTECH #:

# 1. Create a list of your top 5 favorite meals. Call this list 'fav_meals'. Print the third meal on the list.

# Your code here


# 2. Add the meal "poppyseed chicken" to your list, now print the list to make sure this was added properly.

# Your code here


# 3. Create a dictionary called kitchen.  In this dictionary, you will have the following sets of keys and values
    # pantry will include peanut butter, syrup, crackers, and alfredo
    # fridge will include milk, eggs, butter, and shredded cheese
    # meals will be your fav_meals list
    # grocery_list will be a list of items you need to make poppy seed chicken
        # This will include chicken breasts, poppy seeds, sour cream, and cream of chicken soup
    # trips will be a number representing the number of trips you take to go to the grocery store. Set this as 0.
  # print out your dictionary to make sure that your fav_meal list shows all the items created in Question 1 and 2.

# Your code here


# 4. Now you go shopping. You were able to find poppy seeds and sour cream, but you weren't able to find the other 
#    items on your list
    # Update your kitchen dictionary
        # Add poppy seeds to your pantry
        # Add sour cream to your fridge
        # Take both of these items off your grocery_list
        # Update your number of trips
    # Print your dictionary to make sure these updates were incorporated properly

# Your code here


# 5. You find a grocery store that has the rest of the items on your grocery list
    # Update your kitchen dictionary
        # Add cream of chicken soup to your pantry
        # Add chicken breast to your fridge
        # Take both of these items off your grocery_list
        # Update your number of trips
    # Print your dictionary to make sure these updates were incorporated properly

# Your code here


# 6. The student now becomes the teacher!
    # Create a variable called score. We are going to start by assigning this variable the value of 87 (out of 100)
    # Create an if-elif-else statement that will print what the student grade is based on the score variable
        # Scores that are 90 or higher should return the statement 'You got an A'
        # Scores that are 80 to 90 (not including 90 itself) should return 'You got a B'
        # Scores that are 70 to 80 (not including 80 itself) should return 'You got a C'
        # Scores that are 60 to 70 (not including 70 itself) should return 'You got a D'
        # Scores that are less than 60 should return 'You failed'
    # Run this code and the score of 87 should print the statement 'You got a B'.

# Your code here


# 7. Expand on your code from Question 6. Now you are going to write a function named grade.
    # The grade function takes one parameter called 'sscore' short for student score.
    # You should be able to copy your code from question 5 into the function and change 'score' to 'sscore'
    # After you have created your function, test this function using the code grade(75.5)

# Your code here


# 8. Below, I have provided a list that shows the number of stock shares owned by 15 stock shareholders. 
    # The company has grown so much that the shares have split. 
    # Everyone that currently owns stock gets to double their number of shares
        # Use a for loop to multiply all the number of stock by 2
            # Create a new empty list called double_list
            # Start a for loop that iterates through all the items of stock_list
            # Inside the for loop, create a new variable called double_value and set this equal to the iterated value multiplied by 2
            # Add double_value to double_list
            # After you have fun your for loop, print double_list to make sure that each value from stock_list has been doubled

stock_list = [10, 20, 300, 75, 3, 15, 26, 5000, 46, 13, 22, 100, 30, 44, 1000]

# Your code here


# 9. You want to build a game that finds how long it takes for you to collect all of the face cards in a deck of cards. 
    # For our purposes, we will use only one suit of cards numbered 2-14 where 11 = "Jack", 12 = "Queen", 13 = "King", and 14 = "Ace"
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

# Your code here


# 10. Add to your while loop in Question 9. 
    # Add an if statement after you remove the first card from possibilities
    # The if statement should instruct the code to break if cards 11 and 12 and 13 and 14 are in your hand (cards_picked)
    # Change the print statement outside of the for loop to print "Number of picks: #" where number represents the number of cards in your hand.
 

