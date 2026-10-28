# 42. Banking Program

is_running = True
balance = 2

def show_balance():
    print(f"Your balance is {balance}")

def deposit():
    amount = float(input("Enter the amount: "))

    if amount < 0:
        print("Invalid amount")
        return 0
    elif amount == 0:
        return 0
    else:
        return amount

def withdraw():
    withdrawal = float(input("Enter the amount: "))

    if withdrawal > balance:
        print("Insufficient funds")
        return 0
    elif withdrawal < 0:
        print("Invalid amount")
        return 0
    else:
        return withdrawal

while is_running:
    print("1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_balance()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("Invalid choice")