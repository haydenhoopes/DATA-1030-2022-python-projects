# Name:
# BTECH #:

print("********  Question 1  ********")
# This is your very first Python question! Notice that this text is all the same 
# color. That is because each line that starts with a "#" sign is a comment. 
# Comments are ignored by Python, so you can use them to write anything that you 
# want. Write a single line comment of your choosing below.

# Hello! I am a comment


print("\n********  Question 2  ********")
''' 
    This line of text is probably a different color. That's because this text is 
    surrounded by triple quotes, so it's treated as a multi-line comment. Python 
    will ignore multi-line comments too. Turn the haiku below into a multi-line 
    comment by adding triple quotation marks to it.
'''

"""
Oh! Blue screen of death
Fatal error has occurred
I move palm to face 
"""

print("\n********  Question 3  ********")
# In the function `say_hello()` shown below, the text "goodbye" is actually printed 
# out by mistake. To fix this, comment out the line of code that prints out 
# "goodbye", and uncomment the line that prints out "hello".

def say_hello():
    # print("goodbye")
    print("hello")

say_hello()


print("\n********  Question 4  ********")
# Create four new variables of data types integer, float, string, and boolean. You 
# can assign the variables any value you want, as long as they are the correct type.

an_integer = 4
a_float = 4.2
a_string = "what"
a_boolean = False


print("\n********  Question 5  ********")
# Print out the type of each of the four variables from the previous question using 
# the `type()` function. This should be done on four or more lines.

# Whenever you see a comment that says "Your code here", be sure to erase it and put
# your own code instead!

type(an_integer)
type(a_float)
type(a_string)
type(a_boolean)


print("\n********  Question 6  ********")
# Recall that the equation for a line is as follows:
# y = mx + b
# In this function, 'x' and 'y' represent a specific point on a grid. The 'm' 
# represents the slope of the line and 'b' represents where the line crosses the 
# y-axis. If we know the slope 'm', the y-intercept 'b', and 'x', then we can 
# calculate 'y'.

# In the code below, you can see that y is calculated using m=2, x=3, and b=4. 
# However, this code isn't very readable or reusable.

# Recalculate the value of 'y' by creating variables for 'm', 'x', and 'b'. Use 
# the variables in the calculation rather than the numbers.

y = 2 * 3 - 4
print(y)

m = 2
x = 2
b = -4

y = m*x + b
print(y)


print("\n********  Question 7  ********")
# Below is some code that is commented out because it won't run correctly. Why might
# this be? What could be done to fix it? You can write your response inside of the 
# triple quotes below, replacing the text that says "Your answer here."

# first_name = "Tito"
# last_name = "Puente"
# birth_year = 1923
# print(first_name + " " + last_name + " " + birth_year)

'''
    The variable `birth_year` is an integer, which cannot be concatenated to a
    string. The function `str()` should be used on it first.
'''


print("\n********  Question 8  ********")
# The variables below can be created and used just fine. However, some of them are 
# formatted incorrectly, and some use key words that should not be used as variable
# names. Add a comment next to each line to indicate if the variable name is "good",
# "formatted incorrectly", or "uses a key word".

bool = True # Ex. uses a key word
number_of_sushis_eaten_today = 24 # good
hoursuntilthenextuselection = 3879.75 # formatted incorrectly
next = "yes" # uses a key word
PetName = "Milo" # formatted incorrectly
currentCount = 0 # good


print("\n********  Question 9  ********")
# Using the `print()` function, copy and print out the following text:
#   We -> all -> live -> in -> a -> yellow -> submarine

print("We -> all -> live -> in -> a -> yellow -> submarine")


print("\n********  Question 10 ********")
# Using the `print()` function and the `sep=` parameter, print out the following
# text using the variables below:
#   We -> all -> live -> in -> a -> yellow -> submarine

word_1 = "We"
word_2 = "all"
word_3 = "live"
word_4 = "in"
word_5 = "a"
word_6 = "yellow"
word_7 = "submarine"

print(word_1, word_2, word_3, word_4, word_5, word_6, word_7, sep=" -> ")


print("\n********  Question 11 ********")
# Using the variables a, b, and c below, create a string called `big_number` that is
# the number 48335. Use typecasting and string formatting to accomplish this.

a = 3
b = 35
c = 48

big_number = str(c) + str(b) + str(a)


print("\n********  Question 12 ********")
# Print out the variable `big_number` from the previous question. You should see the
# number 48335 printed out.

print(big_number)


print("\n********  Question 13 ********")
# Turn the variable `truth` into an f-string and replace the `?` with Batman's real
# identity by placing the variable inside of the string inside curly braces. Then,
# print out the variable `truth`.

real_identity = "Bruce Wayne"
truth = f"Batman's real identity is {real_identity}."


print("\n********  Question 14 ********")
# Three of the names below are names of the Jonas brothers. Finish the string
# `j_brothers` below by inserting the correct `name` variables into the f-string,
# replacing the question marks.

# You can look up the names online if you aren't sure what they are.


name_1 = "Benjamin"
name_2 = "Joe"
name_3 = "Harvey"
name_4 = "Kevin"
name_5 = "Nick"

j_brothers = f"The Jonas brothers' names are {name_2}, {name_4}, and {name_5}."

print(j_brothers)