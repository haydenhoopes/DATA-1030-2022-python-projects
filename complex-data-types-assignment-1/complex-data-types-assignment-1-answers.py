# Name: 
# BTECH #: 


# 1. Create a new list called world_flags. Give this list strings of at least five countries whose flags you like.
#    Print out the type of world_flags to make sure it's a list.

world_flags = ['United States of America', 'Colombia', 'Japan', 'Spain', 'Cuba']
print(type(world_flags))


# 2. Use indexing to access the second flag in your list world_flags. Remember that in Python, indexes
#    start with 0, so the second item would be at index 1. Print out that flag.

second_flag = world_flags[1]
print(second_flag)


# 3. Print out the length of your list world_flags using the len() function.

length_of_flags_list = len(world_flags)
print(length_of_flags_list)


# 4. Add "Mars" to the world_flags list using the .append() method. Print out world_flags to make sure
#    Mars was added correctly.

world_flags.append("Mars")
print(world_flags)


# 5. Use the .sort() method on the list and print it out. Notice that the list is now sorted alphabetically!

world_flags.sort()
print(world_flags)


# 6. Create a new dictionary called my_dream_car. Make up attributes for the car as keys in the dictionary, and give
#    them appropriate values. You must at least give my_dream_car a make (string), year (integer), mpg (float),
#    model (string), and a list of places you want to take the car (list of strings).

my_dream_car = {
    "make": "Chevrolet",
    "year": 2007,
    "mpg": 32.4,
    "model": "Aveo",
    "places_to_go": ['Salt Lake City', 'Logan', 'Boise']
}


# 7. Print out the year, make, and model of my_dream_car by accessing the keys of the dictionary in a single
#    print statement. Then print out the first location of the list of places you want to take the car.

print(my_dream_car['year'], my_dream_car['make'], my_dream_car["model"])
print(my_dream_car['places_to_go'][0])



# 8. Add a new attribute to the my_dream_car dictionary called "miles". Assign it a float value that makes sense.
#    Then, remove the key "mpg" from the dictionary. Print out my_dream_car.

my_dream_car["miles"] = 98454.1
my_dream_car.pop("mpg")
print(my_dream_car)


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

print(space_shuttles)
space_shuttles.pop()
space_shuttles.append("The Millenium Falcon")
space_shuttles.sort()
print(space_shuttles)


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
mean = sum(numbers) / len(numbers)
median = numbers[len(numbers) // 2]
print(mean)
print(median)

# 11. Check out the items in your backpack! This dictionary represents your inventory:
#     Several things happened to you today. Update the dictionary accordingly.
#    a. You bought a pet hamster and have to keep it in your backpack since you're at work.
#       Add the key "pet" with a value of "hamster" to the backpack.
#    b. Your hamster then ate all the Skittles. Remove them from the list of snacks.
#    c. At the end of the day, you need to spend $2.00 to buy some wood shavings. Print out how much
#       money you have. Then, subtract the $2.00 from the money in the backpack.
#    d. Print out the final dictionary to see what you ended up with.

backpack = {
    "car_keys": True,
    "money": 4.18,
    "diapers": 3,
    "snacks": ["Goldfish", "Skittles", "Bottled Water"]
}

# Your code here
backpack['pet'] = "hamster"
backpack['snacks'].remove("Skittles")
print(backpack['money'])
backpack['money'] = backpack['money'] - 2
print(backpack)
