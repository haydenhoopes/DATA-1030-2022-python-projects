current_year = 2022

if current_year == 2020:
    print("It's gonna be a rough year")
elif current_year < 2010:
    print("Ah. The good ol' days.")
else:
    print("time to be optimistically cautious")


def circumference(r):
    return r * 2 * 3.14159

radius = 7

if circumference(7) > 100:
    print("It's a big ol' circle")
else:
    print("tiny circle")


my_name = "Kyle"

if my_name == "Hayden" and current_year == 2022:
    print("Hello self.")

if my_name == "Hayden" or current_year == 2022:
    print("Either it's 2022 or I am Hayden")

if my_name != "Hayden":
    print("name not hayden")

if my_name is not "Hayden":
    print("name not Hayden")

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)


phrase = "when the saints come marching in"

# print("saint" in phrase)
if "saint" in phrase:
    print("Halleluyah!")
else:
    print("sad")