### WAR
# Name: 
# BTECH #:

# In this project, you will create the game "War" in which the user plays against the computer to win battles. 
# Winning a battle involves playing a higher card than the other person, with the Ace being the high card. 
# Cards cannot be reused and the player who wins the most battles when the cards run out is the winner.

# Note that in this version of "War", there is only one suit and thus, only one of each card.
# 5 is a 5 value, and 11 is a Jack, 12 is a Queen, and 13 is a King. The number 14 is an Ace, which is the 
# highest value card.

import random

from matplotlib.style import use # To distribute the cards randomly, we will import the random module.
deckOfCards = [i for i in range(5,15)] # Create the deck of cards, which is really just a list of numbers 2-14
random.shuffle(deckOfCards) # Mix up the order of the deckOfCards using the shuffle method 


# Question 1: Create `user` dictionary and print it out. The dictionary will have three keys:
#   - name: a single string of your name
#   - winCount: starts as an integer 0
#   - cardList: a list derived as a subset of the `deckOfCards` list. Since there are 10 cards total (and they
#     are already shuffled), give yourself the first 5 cards in deckOfCards. The first 5 cards can be accessed
#     using the code `deckOfCards[0:5]`.
#       • Print out the dictionary `user` to make sure this was created properly.

user = {
    "name": "BTECH",
    "winCount": 0,
    "cardList": deckOfCards[0:5]
}
# print(user) # Commented out in Question 10


# Question 2: Create `computer` dictionary and print it out. The dictionary will have the same three keys as
# before:
#   - name: a single string of the computer's name
#   - cardList: a list derived as a subset of the `deckOfCards` list. Since there are 10 cards total (and they
#     are already shuffled), give the computer the last 5 cards in deckOfCards. The last 5 cards can be accessed
#     using the code `deckOfCards[5:10]`.
#       • Print out the dictionary `computer` to make sure it was created properly.
#       • Print `deckOfCards` and check that the user `cardList` contains the first five cards and the computer 
#         `cardList` contains the last 5 cards. Note that these cards will change each time the code is run so 
#         this isn't considered cheating to look at the cards at this stage.

computer = {
    "name": "Robot",
    "winCount": 0,
    "cardList": deckOfCards[5:10]    
}

# print(computer) # Commented out in Question 10
# print(deckOfCards) # Commented out in Question 10


# Question 3: Create a while loop that will run as long as the number of cards in the user's card list is greater 
# than 4. We will eventually change this statement, but for now, we just want to see the while loop run once as 
# we "remove a card" from the player's hand. If you run your code before finishing Question 3, you risk creating
# an infinite loop that may not ever stop. If this does happen to you, click the Command Prompt and then Ctrl+C
# until the program terminates.
#   - Inside the loop, print out the user's `cardList`. This will show the user what cards are in their hand.
#   - Create a variable called `userCard`. This variable will require user input. Ask the user, "Which card do
#     you want to play?". Remember that this input must be converted to an integer.
#   - Remove the `userCard` from the user's `cardList` using the `.remove()` method.
#   - Print the user's `cardList`
#       • Run the code and make sure that you see the list of cards in your hand and are asked which card you want
#         to play. After inputting a value from the lsit of 5 cards, you will see the list of cards with the
#         card that the user chose removed. Finally, because the length of the list is no longer greater than 4, 
#         the while loop will end.

while len(user["cardList"]) > 0: # Was `> 4` before Question 10
    print(user["cardList"])
    userCard = int(input("Which card do you want to play? "))
    user["cardList"].remove(userCard)
    # print(user["cardList"])


# Question 4: Eventually, we will want to take out our print statements since we will know our code is running
# properly. But we will want to add useful notes when the print statements are gone.
#   - Add a statement in your while loop that prints "You chose #." where # represents the number the user chose 
#     to play ('userCard')
#       • Run your code again and make sure this this outputs correctly. Note that you may need to convert the
#         user's card to a string.
#       • Don't forget that code inside the while loop is indented. Even though it may be separated by comments
#         that are not indented, the code still needs to be indented properly (comments are completely ignored).

    print("You chose the number " + str(userCard))


# Question 5: Now you will add the computer's choice.
#   - Print the computer `cardList`.
#   - Create a new variable called 'computerCard'.  This variable will select the first card in the computer's 
#     'cardList' (since these cards were previously randomized). The index starts at 0.
#   - Remove the card `computerCard` from the computer `cardList`.
#   - Print the `computerCard`.
#   - Print the computer `cardList`.
#       • Run your code again and make sure you see the computer's original hand of cards, the card chosen, 
#         and the hand of cards now that this 'ComputerCard' has been played. 
    
    # print(computer["cardList"])
    computerCard = computer["cardList"][0]
    computer["cardList"].remove(computerCard)
    # print(computerCard)
    # print(computer["cardList"])


# Question 6: Before we drop most of these print statements, let's add a note of what card the computer played.
#   - Add a statement in your while loop that prints "Name of computer chose #" that shows which card the computer
#     chose. You may need to convert `computerCard` to a string before printing.
#       • Run your code again and make sure that everything prints out correctly.

    print("The computer chose the number " + str(computerCard))


# Question 7: We now need to limit what gets printed to the console. In the actual game of War, the user shouldn't
# be able to see which cards the computer has and is going to play.
#   - Comment out all print statements EXCEPT for the user's `cardList`, the statement `You chose the number + #`,
#     and the statement `The computer chose the number #`.
#       • Run your code again. This time, you should only see your hand, be asked to select a card from your hand,
#         see the statement `You chose the number #`, and see the statement `The computer chose the number #`.

# No code necessary here


# Question 8: Now it's time to see who wins the battle for the first iteration of the while loop. Whoever played
# the highest card wins the battle.
#   - Compare the user card and the computer card in an if statement. If your card is higher than the computer's
#     card, print out "You won the battle!". Otherwise, print out "You lost the battle".
#       • Run your code and you should see either "You won the battle!" or "You lost the battle" as a final print
#         statement. Make sure the comparison worked properly (ie. 13 actually did beat 7, etc.)

    if userCard > computerCard:
        print("You won the battle!")
        user["winCount"] += 1 # Question 9
    else:
        print("You lost the battle.")
        computer["winCount"] += 1 # Question 9


# Question 9: Make sure that the battle wins get added to the win count in either the user or the computer's
# dictionary.
#   - Add a line to your if statement that if you win the battle, 1 gets added to the user dictionary `winCount` 
#     and is reassigned. If the computer wins, 1 gets added to their `winCount` and is reassigned.
#   - Print the user's `winCount` and the computer's `winCount` after the if statement.
#       • Run the code and make sure that the winner of the battle shows 1 as their win count and the loser shows
#         0 as their win count.

# Modify code from Question 8. Then, add your code here.

    # print(f"{user['name']} has {user['winCount']} wins and {computer['name']} has {computer['winCount']} wins.")


# Question 10: Now we will remove the limiting condition of the while loop to play battles until no cards are left.
#   - Change the condition in the while loop (first line) to run while the length of the user's `cardList` is 
#     greater than 0. This means that while cards are still left, the loop will keep running.
#   - There are five cards in each hand. Thus, five "battles" should be played.
#       • Run the code and this time you should be asked what card you want to play 5 different times. Make sure
#         that the win counts are added up properly.

# No code necessary here. Modify code from Questions 2 and 3.


# Question 11: Now that we know the code is working, let's not worry about seeing the count of wins each round (we
# just want to see the total at the end). Comment out the print statement from Question 10 that prints out the
# number of wins each player has.

# No code necessary here. Modify code from Question 10.


# Question 12: The while loop is now completed. Now you can run through the entire game and determine a winner and
# a loser.
#   - After the while loop (not indented), write an if statement that compares the user's `winCount` to the 
#     computer's `winCount`. If the user's `winCount` is greater, print "(Name of user) wins!". Otherwise, print
#     "(Name of computer) wins." where (Name of user/computer) represents the name given in their dictionary.
#       • Run the code to make sure you can play the game and declare a proper winner.

if user["winCount"] > computer["winCount"]:
    print(f'{user["name"]} wins!')
else:
    print(f'{computer["name"]} wins.')
