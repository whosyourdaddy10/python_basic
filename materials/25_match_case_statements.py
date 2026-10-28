# 37. Match Case Statements = Switch Case Statements

# name = input("Enter your name: ")

# match name:
#     case "Rahfi":
#         print("Hello Rahfi")
#     case "John":
#         print("Hello John")
#     case "Jane":
#         print("Hello Jane")
#     case _:
#         print("Hello")

is_weekend = input("Enter the day: ")

match is_weekend:
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Weekday")