# 43. Slot Machine Program

import random

def spin_row():
    symbols = ['🍉', '🍎', '🍇', '🍊', '⭐']

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("|".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍉':
            return bet * 3
        elif row[0] == '🍎':
            return bet * 4
        elif row[0] == '🍇':
            return bet * 5
        elif row[0] == '🍊':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0

def main():
    balance = 100

    print("Welcome to the slot machine!")
    print("Symbols: 🍉🍎🍇🍊⭐")

    while balance > 0:

        print(f"Balance: {balance}")

        bet = input("Enter your bet: ")

        if not bet.isdigit():
            print("Please enter the valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("You don't have enough balance")

        if bet <= 0:
            print("Invalid bet")

        balance -= bet

        row = spin_row()
        print("Spinnig...")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            balance += payout
            print(f"You won ${payout}")
        else:
            print("You lost")

        play_again = input("Do you want to play again? (Y/N): ")

        if play_again.lower() != "y":
            break

    print(f"Your balance is {balance}")        
    print("Thanks for playing!")
    
if __name__ == "__main__":
    main()