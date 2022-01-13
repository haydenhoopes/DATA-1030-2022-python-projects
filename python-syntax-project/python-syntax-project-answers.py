# Name: 
# BTECH #:

#  ********  QUESTION 1  ********
# Make a function called luckyNumber() that accepts three parameters:
#   fName: A person's first name
#   lName: A person's last name
#   luckyNumber: A lucky number
# This function should print out the person's full name and state their 
# lucky number. Be sure to use the print() function!
# Below the function definition, call the function using made up values
# to show that the function works.

def luckyNumber(fName, lName, number):
    print(f"My name is {fName} {lName} and my lucky number is {number}")

luckyNumber("Hayden", "Hoopes", 24)

# ********  QUESTION 2  ********
# Make two functions: circumferenceOfCircle() and areaOfCircle().
# Each function returns and prints the circumference of a circle given a 
# radius. You can use the variable PI as an approximation of pi.
# Below each function definition, call the function using a made up value
# to show that it works.

PI = 3.141592

def circumferenceOfCircle(r):
    print(f"The radius of the circle is {r} and the circumference is {PI * r * 2}")
    return PI * r * 2


circumferenceOfCircle(20)


def areaOfCircle(r):
    print(f"The radius of the circle is {r} and the area is {PI * r ** 2}")
    return PI * r ** 2

areaOfCircle(14)


# ********  QUESTION 3  ********
# Make a function called typeOfVariable() that accepts a single variable.
# This function should print (not return) the variable and its type.
# Below the function definition, call the function using a made up variable
# to show that it works.

def typeOfVariable(variable):
    print(f"The variable is {variable} and its type is {type(variable)}")

typeOfVariable(True)
