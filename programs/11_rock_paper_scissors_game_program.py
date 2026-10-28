# 29. Rock, Paper, Scissor Game
import random

options = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(options)

    player = input("Enter a choice (rock, paper, scissors): ").lower()

    while player not in options:
        print("Invalid choice")
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"Computer: {computer} Player: {player}")
    if player == computer:
        print("Tie")
    elif player == "rock" and computer == "scissors":
        print("You win")
    elif player == "paper" and computer == "rock":
        print("You win")
    elif player == "scissors" and computer == "paper":
            print("You win")
    else:
        print('You lose')
        running = False

    play_again = input("Play again? (y/n): ").lower()
    while play_again not in ("y", "n"):
        play_again = input("Play again? (y/n): ").lower()
    
    if play_again != "y":
        running = False

print("Thanks for playing")