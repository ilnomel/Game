#This is a guessing game code

import random

print("Hi! I'm thinking of a random number between 1 and 100.")

attempt = 0

my_number = random.randrange(1,101)
for i in range(10):
    attempt += 1
    print("--- Attempt %d" % attempt)
    guess = int(input("Guess what number I am thinking of: "))
    if guess > my_number:
        print("Too high.")
    if guess < my_number:
        print("Too low.")
    if guess == my_number:
        print("Congradulations! You guessed correctly!")
        break
print("Aw, you ran out of tries. The number was %d" % my_number)