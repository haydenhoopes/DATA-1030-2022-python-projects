import random

words = ["apple", "banana", "watermelon"]
random.shuffle(words)

word_to_guess = words[0]

print("Welcome to Hangman © 2022")

while True:
    number_of_letters = len(word_to_guess)
    # Code not finished -- out of scope for module 2

    user_guess = input("Guess a letter: ")
