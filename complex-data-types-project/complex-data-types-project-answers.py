### WAR
# Name: 
# BTECH #:

# In this project, you will create the game "War" in which the user plays against the computer to try and capture all of their cards.
# Note that in this version of "War", there is only one suit and thus, only one of each card.
# 2 is a 2 value, and 11 is a Jack, 12 is a Queen, and 13 is a King. The number 14 is an Ace, which is the highest value card.
# NOTE: This game is obviously unfair, since the person who gets the 14 can't be beat and will always win. You can try to solve
# this problem in your code if you'd like, but it's not a requirement.

# Create the cards, which are really just numbers 2-14
deckOfCards = [i for i in range(2,15)]

# Create the user and the computer as dictionaries
# Each person should have a name (string), a count of wins (integer), and a list of cards (list)
# The name can be anything you'd like, but the wins should be 0 and the list of cards should be empty for now.

computer = {
    "name": "Darth Vader",
    "cards": [],
    "wins": 0
}

user = {
    "name": "Hayden",
    "cards": [],
    "wins": 0
}

# Distribute the cards to each of the players
# To distribute the cards randomly, we will import the random module.
import random

# Mix up the order of the variable called deckOfCards using the shuffle method from the random module
random.shuffle(deckOfCards)

# Now that the deckOfCards is shuffled, start handing out cards, alternating between the user and computer.
# To 'hand out' a card, pop an item out of the list and append it to the "cards" of the corresponding dictionary.
# Use a for loop with the range function to walk through each card and pop it into the computer or user.
# One strategy for deciding whether to give the card to the user or to the computer is if the iteration is odd or even.

for i in range(len(deckOfCards)):
    if i % 2 == 0:
        computer['cards'].append(deckOfCards.pop())
    else:
        user['cards'].append(deckOfCards.pop())

# The cards have been assigned, now it's time to start the game with a while loop. Actually, there will be 
# two while loops. The first one will determine if the user wants to play another game. The second while
# loop will determine if either player has captured all of the cards of the other person.

# This variable allows the while loop to continue functioning until the user decides to stop playing.
stillPlaying = True
while stillPlaying:
    # Here, we print out the number of wins for the user and the computer.
    print(f"{computer['name']} has {computer['wins']} wins and {user['name']} has {user['wins']} wins.")

    # The second while loop will check whether the length of either the computer cards list or the user
    # cards list is empty. If either is empty, the game is over, and the person who does not have an empty list
    # will have 1 added to their wins!
    while len(computer['cards']) != 0 and len(user['cards']) != 0:

        # This code will run on each turn. Each turn we will 1) present the user their cards, 2) allow them to
        # choose a number by typing it in the console and 3) make the computer choose a card. We will then 4)
        # compare the cards to each other. If the user's card is greater than the computer's card, both the user's
        # card and the computer's card get added to the user's cards. The opposite is also true.

        # The turn will then end and the while loop will check to see if either list of cards is empty. If neither
        # is empty, another turn will take place.

        # 1) Show the user their cards
        print(f"You have the cards {user['cards']}")

        # 2) Get the user's input, what card do they want to use?
        # Here we will also pop this number out of the user card list and store it in a variable.
        # IMPORTANT: You may want to use another while loop here to make sure that the user doesn't enter in
        # an invalid number, like 'a'.
        userSelectionConfirmed = False
        while not userSelectionConfirmed:
            userSelection = input("Which card do you want to use? ")
            if userSelection.isnumeric() and int(userSelection) in user['cards']:
                userSelection = int(userSelection)
                print(f"You chose {userSelection}")
                user['cards'].remove(userSelection)
                userSelectionConfirmed = True
            else:
                print("That's not a valid choice. Try again.")

        # 3) Get the computer's card selection using the choice method of the random module
        computerSelection = random.choice(computer['cards'])
        computer['cards'].remove(computerSelection)

        # 4) Compare the cards. Don't forget to print out what is happening to the console!
        print(f"{computer['name']} chose {computerSelection}")
        if userSelection == 14 and computerSelection == 2:
            computer['cards'].append(userSelection)
            computer['cards'].append(computerSelection)
            print("You lost this round!")
        elif userSelection == 2 and computerSelection == 14:
            user['cards'].append(userSelection)
            user['cards'].append(computerSelection)
            print("You won this battle!")
        elif userSelection > computerSelection or (userSelection == 2 and computerSelection == 14):
            user['cards'].append(userSelection)
            user['cards'].append(computerSelection)
            print("You won this battle!")
        else:
            computer['cards'].append(userSelection)
            computer['cards'].append(computerSelection)
            print("You lost this round!")

        # Now the turn is over. Because of the while loop, the turns will only stop occuring once one of the players
        # runs out of cards.

    # When a player runs out of cards, the code will come here. Add a win to the corresponding player
    # and then ask the user if they want to keep playing. If they want to stop, set the stillPlaying
    # variable to False
    if len(user['cards']) == 0:
        computer['wins'] += 1
        print("You lost the war!\n")
    else:
        user['wins'] += 1
        print("You won the war!!!\n")

    playAgain = input("Do you want to play again (y/n)? ")
    if playAgain == "n":
        stillPlaying = False
        print("Thanks for playing!")
    else:
        # If the player does want to play again, make sure to reshuffle the deck and reassign their cards.
        # You can copy the code from above to do this.
        deckOfCards = [i for i in range(2,15)]
        random.shuffle(deckOfCards)
        computer['cards'] = []
        user['cards'] = []
        for i in range(len(deckOfCards)):
            if i % 2 == 0:
                computer['cards'].append(deckOfCards.pop())
            else:
                user['cards'].append(deckOfCards.pop())
