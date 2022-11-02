from turtle import distance


def hello(number, name="user"):
    print("hello, " + name + " your favorite number is " + str(number))

hello(4)
hello(name="Hayden", number=24)



def absolute_value(n):
    if n < 0:
        return -n
    else:
        return n

print(absolute_value(-5))
absolute_value(30)

current_temperature = 90
print("The absolute value of the temp is " + str(absolute_value(current_temperature)))


favorite_number = 9

def square_root(n):
    return n ** 0.5


print(square_root(4))
print(square_root(16))
print(square_root(favorite_number))


def recursion():
    print("Recursion is the gift that keeps on giving")
    recursion()

#recursion()



def distance_between_two_points(x1, y1, x2, y2, method="euclidean"):
    if method == "manhattan":
        return absolute_value(x1 - x2) + absolute_value(y1 - y2)
    elif method == "euclidean":
        return square_root( (x2 - x1)**2 + (y2 - y1)**2 )

m_distance = distance_between_two_points(0, 0, 4, 3, method="manhattan")
e_distance = distance_between_two_points(0, 0, 4, 3)

print(m_distance)
print(e_distance)