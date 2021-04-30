import random

print("Number guessing Game")

number = random.randint(1, 9)

chances = 0

while chances < 5:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations, You guessed it right")
        break

    elif guess < number:
        print("You gotta guess higher")

    else:
        print("You gotta guess lower")

if not chances < 5:
    print("Try agin later, you lose")