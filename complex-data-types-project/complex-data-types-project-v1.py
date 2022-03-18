### WAR
# Name: 
# BTECH #:

# In this project, you will create the game "War" in which the user plays against the computer to try and capture all of their cards.
# Note that in this version of "War", there is only one suit and thus, only one of each card.
# 2 is a 2 value, and 11 is a Jack, 12 is a Queen, and 13 is a King. The number 14 is an Ace, which is the highest value card.
# The only card that can beat the Ace (14) is the 2.

import random # To distribute the cards randomly, we will import the random module.
deckOfCards = [i for i in range(2,15)] # Create the deck of cards, which is really just a list of numbers 2-14
random.shuffle(deckOfCards) # Mix up the order of the deckOfCards using the shuffle method 

# Your code here
