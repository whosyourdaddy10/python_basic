# 22. Shopping card Program

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input("Enter the price: "))
        foods.append(food)
        prices.append(price)
        total += price

print("---- YOUR CART ----")

for food in foods:
    print(f"{food}: ${prices[foods.index(food)]}")

print(f"Total: ${total}")
