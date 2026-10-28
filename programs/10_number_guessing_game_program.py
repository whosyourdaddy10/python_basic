# 28. Number Guessing Game
import random

lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number, highest_number)
guesses = 0
is_running = True

while is_running:
    guess = int(input("Enter a number: "))
    guesses += 1

    if guess < answer:
        print("Too low")
    elif guess > answer:
        print("Too high")
    else:
        print(f"You guessed it in {guesses} guesses")
        is_running = False


