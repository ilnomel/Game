import random

print("""Welcom to Camel!
You have stolen a camel to make your way across the great Mobi desert.
The natives want their camel back and are chasing you down! Survive your desert trek and out run the natives.
""")

#new boolean variable
done = False

miles_traveled = 0
thirst = 0
camel_tiredness = 0
canteen_drinks = 10

#natives are 20 miles back
native_distance = -20

while not done:
    print("""
    A. Drink from your canteen
    B. Ahead moderate speed
    C. Ahead full speed
    D. Stop for the night
    E. Status check
    Q. Quit""")

    user_choice = input("Your choice? ")
    
    if user_choice.upper() == "Q":
        done = True
    elif user_choice.upper() == "E":
        print("""
        Miles traveled: %d
        Drinks in canteen: %d
        The natvies are %d miles behind you""" % (miles_traveled, canteen_drinks, -native_distance))
    elif user_choice.upper() == "D":
        camel_tiredness = 0
        print("Camel is happy")
        native_distance += random.randrange(7, 15)
    elif user_choice.upper() == "C":
        miles_traveled = random.randrange(10,21)
        
    
    