import random
secretNumber = random.randint(1, 10)
print("I'm thinking of a secret number between 1 and 100...")
a = 0
while a < 10:
    if input
    guess = int(input("What is your guess? "))
    if (guess == secretNumber):
        break
    elif (guess > secretNumber):
        print("Sorry, your guess is too high.")
    elif (guess < secretNumber):
        print("Sorry, your guess is too low.")
print("You got it!")