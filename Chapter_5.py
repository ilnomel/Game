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
native_distance = -50

#one in 20 chance of finding oasis
oasis = 0

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
    
    #choosing status check
    elif user_choice.upper() == "E":
        print("""
        Miles traveled: %d
        Drinks in canteen: %d
        The natvies are %d miles behind you""" % (miles_traveled, canteen_drinks, -native_distance))
    
    #choosing to stop for the night
    elif user_choice.upper() == "D":
        camel_tiredness = 0
        print("Camel is happy")
        native_distance += random.randrange(7, 15)
    
    #running at full speed
    elif user_choice.upper() == "C":
        miles_traveled += random.randrange(10,21)
        print("You've travelled: ", miles_traveled)
        thirst += 1
        camel_tiredness += random.randrange(1,4)
        native_distance += random.randrange(7, 15)
    
    #walking at moderate speed
    elif user_choice.upper() == "B":
        miles_traveled += random.randrange(5, 13)
        print("You've travelled: ", miles_traveled)
        thirst += 1
        native_distance += random.randrange(7, 15)
    
    #drink from canteen
    elif user_choice.upper() == "A":
        if canteen_drinks > 0:
            canteen_drinks -= 1
            thirst -= 1
        else:
            print("You have no drink left!")
   
    #die of thirst
    if thirst > 4 and thirst <= 6:
        print("You are thirsty")
    elif thirst > 6:
        print("You died of thirst!")
        done = True
   
    #camel dies
    if camel_tiredness > 5 and camel_tiredness <= 8:
        print("Your camel is getting tired")
    elif camel_tiredness > 8:
        print("Your camel is dead.")
        done = True
   
    #natives catch up to you
    if -native_distance <= 0:
        print("You've been caught by the natives!")
        done = True
    elif -native_distance < 15:
        print("The natives are getting close!")
    
    #winning condition
    if miles_traveled >= 200:
        print("You've won the game!")
        done = True
    
    #found oasis
    if oasis == random.randrange(1,21):
        print("You've found an oasis!")
        canteen_drinks = 10
        thirst = 0
        camel_tiredness = 0
    
    