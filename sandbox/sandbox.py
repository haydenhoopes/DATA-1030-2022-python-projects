# Hayden Hoopes
# hhoopes@btech.edu

# Comments
'''
    This is a 
    multiline
    comment
'''

# Variables
pi = 3.141592
pi = "hello"

# Data Types
integer = 3
floatt = 3.24
string = "blah blah blah"
boolean = True
Non = None
listt = [3, "hello", True, string]
dictionary = {"name": "Hayden"}

# Arithmatic Operators
2 + 5
8 - 5
8 * 4
19 /4
2 ** 2
7 // 3
6 % 4
4 ** .5

# Combining Strings
firstname = "Hayden"
lastname = "Hoopes"
#print(firstname + " is the best " + lastname)
#print(f"{firstname} is the best {lastname}")

# Creating functions
def addTwoNumbers(num1, num2):
    print(num1 + num2)
    return num1 + num2

# addition = addTwoNumbers(5, 7)
# print(addition)

# Type casting
int1 = 55
int2 = "74"

# print(int1 + int(int2))
str()
float()
list()
int()
bool()


# ********  COMPLEX DATA TYPES  ********
# Lists
heroes = ["Martin Luther King Jr.", "George Washington", "Steve Carrel"]
print(heroes[0])

# Dictionary
myStuff = {"candy": "Skittles", "numberOfKeyboards": 1, "hasInternet": True}
print(myStuff['candy'])

# Tuple
tupl = (3, "Hello", False)
print(tupl[1])

# Set
uniqueNumbers = {3, 3, 4, 5, 6, 7, 3, 3, 1, "Aliens"}
print(uniqueNumbers)

# For loops and the range function
listOfFruits = ['mango', 'watermelon', 'apple', 'banana', 'cantelope']
iLikeIt = [True, True, False, False, True]
print(len(listOfFruits))

for index in range(len(listOfFruits)):
    print(f"I like the {listOfFruits[index]}: {iLikeIt[index]}")

# While loop
total = 0
stillAdding = True
# while stillAdding:
#     num = int(input("What number to add? "))
#     total += num
#     print(f"The current total is {total}")
    
#     keepGoing = input("Do you want to keep adding? (y/n) ")
#     if keepGoing == "y":
#         pass
#     else:
#         stillAdding = False

# If statements
happy = 54
if happy == True:
    print("You are happy!")
elif happy == False:
    print("So sad")
else:
    print("That was not clear")