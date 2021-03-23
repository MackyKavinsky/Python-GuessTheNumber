import random

n = random.randint(1,15)

guess = int(input("Guess the number please: "))

while n != guess:
    if guess>n:
        print("Guess is too high!")
        guess = int(input("Please guess the new number: "))
    elif guess<n:
        print("Guess is too low!")
        guess = int(input("Please guess the new number: "))
    else:
        print("You guess the right number!")
        break