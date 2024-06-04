# this is the guess the number game
import random
secret_number = random.randint(1, 20)
print("i'm thinking of a number between 1 and 20")

# ask the player to guess 6 times
for guesses_taken in range(1, 7):
    print("take a guess")
    guess = int(input())

    if guess < secret_number:
        print("your guess is too low")
    elif guess > secret_number:
        print("your guess is too high")
    else: 
        break # this condition is the correct guess

    if guess == secret_number:
        print("good job!")
        print("you guessed my number in " + str(guesses_taken) + " guesses!")
    else:
        print("nope. the number i was thinking of was " + str(secret_number))