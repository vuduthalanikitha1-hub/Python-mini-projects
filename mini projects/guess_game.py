import random

secret_number = random.randint(1, 10)

print("Number Guessing Game")
print("Guess a number between 1 and 10")

guess = int(input("Enter your guess: "))

if guess == secret_number:
    print("Correct! You won!")

else:
    print("Wrong number")
    print("The correct number was", secret_number)