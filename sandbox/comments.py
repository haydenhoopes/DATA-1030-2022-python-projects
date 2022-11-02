# laskejf lsklks ejflksjlksjefl kasjeflkasjeflkasjflksa
#sflaskjf skfdjl 
#this is a comment

# asdflka sjd
# asdlfj saldkslfdkjaslekf
# alsfk jsalekfj

'''
asldfk jaselkfj
aselkfjaslekfj
askdlfj
asdlfkjalekfjalsekfjalskefjlaskej
'''

"""
dfjglsdkjrglsd
sdlgkjsdlkgjsdlkgjlskdfgjlskdfja
alsdkfjlas
"""
# This function solves the quadratic function
def q(a, b, c):
    import math

    # 'd' is the discriminant
    d = b**2-4*a*c

    # If d is less than 0, there are no solutions
    if d < 0:
        return False
    
    # If d is equal to 0, there is exactly one solution
    elif d == 0:
        x = (-b+math.sqrt(b**2-4*a*c))/2*a
        return (x)
    
    # If d is greater than 0, there are two solutions
    else:
        x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
        x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
        return (x1, x2)


print(1 + 1)
# print("a" + 1)
print(3 + 3)

