# Name: 
# BTECH #: 


# 1. Create a new list called flags_of_the_world. Give this list strings of at least five countries whose flags you like.

# Your code here


# 2. Use indexing to access the second flag in your list flags_of_the_world. Remember that in Python, indexes
#    start with 0, so the second item would be at index 1. Print out that flag.

# Your code here


# 3. Print out the length of your list flags_of_the_world using the len() function.

# Your code here


# 4. Add "Mars" to the flags_of_the_world list using the .append() method.

# Your code here


# 5. Print out the flags_of_the_world list. Then, use the .sort() method on the list and print it again.

# Your code here


# 6. Create a new dictionary called my_dream_car. Make up attributes for the car as keys in the dictionary, and give
#    them appropriate values. You must at least give my_dream_car a name (string), year (integer), mpg (float),
#    brand (string), and a list of places the car has been to (list of strings).

# Your code here


# 7. Print out the name and the year of my_dream_car by accessing the keys of the dictionary.

# Your code here


# 8. Add a new attribute to the my_dream_car dictionary called "miles". Assign it a float value that makes sense.
#    Then, remove the key "brand" from the dictionary.

# Your code here


# 9. Given the following list of space shuttles:
#   a. Print out the list
#   b. Use the .pop() method to remove the last shuttle in the list.
#   c. Use the .append() method to add "The Millenium Falcon" to the list.
#   d. Use the .sort() method to sort the names of the space shuttles.
#   e. Print out the list again, now sorted alphabetically.

space_shuttles = [
    'Endeavour',
    'Columbia',
    'Discovery',
    'Atlantis',
    'Challenger',
    'Tardis'
]

# Your code here


# 10. Using the following list of numbers:
#    a. Use the len() and sum() functions to compute the mean of the set of numbers.
#       Remember that mean can be computed as sum / length of list (number of observations)
#    b. Get the median value. Remember that median is the middle value of a sorted list, computed as
#       the nth value in the list where n is len() // 2 (integer division).
#       Hint: The length of the list is 37. That means that if you divide by 2 (to get the position of the middle number),
#       you will get 18.5. Unfortunately, you can't use a decimal number as an index! Furthermore, the
#       number 19 will actually return the number in position 18 (since the first item is 0, then 1, etc.).
#       By using floor division (//) we can automatically get 18.5 and round it down, getting the correct index
#       for item 17 (the middle number).
#    c. Print out the mean and median. (The mean is 21, the median is 7)

numbers = [5,5,8,2,9,1,100,34,2,6,7,7,7,3,1,6,60,76,7,2,9,85,3,8,5,23,0,3,69,35,50,3,3,86,1,1,45]

# Your code here


# 11. Check out the items in your backpack! This dictionary represents your inventory:
#     Several things happened to you today. Update the dictionary accordingly.
#    a. You bought a pet hamster and have to keep it in your backpack since you're at work.
#       Add the key "pet" with a value of "hamster" to the backpack.
#    b. Your hamster then ate all the Skittles. Remove them from the list of snacks.
#    c. At the end of the day, you need to spend $2.00 to buy some wood shavings. Print out how much
#       money you have. Then, subtract the $2.00 from the money in the backpack.
#    d. Print out the final dictionary to see what you ended up with.

backpack = {
    "carKeys": True,
    "money": 4.18,
    "diapers": 3,
    "snacks": ["Goldfish", "Skittles", "Bottled Water"]
}

# Your code here
