# 26. Comcession Stand Program

menus = {
    "pizza": 3.00,
    "pasta": 2.50,
    "salad": 1.50,
    "soup": 1.00,
    "sandwich": 2.00,
    "juice": 1.50,
    "water": 1.00
}

cart = []
total = 0

for key, value in menus.items():
    print(f"{key}: ${value}")

while True:
    item = input("Enter the item (q to quit): ")
    if item.lower() == "q":
        break
    elif menus.get(item) is not None:
        cart.append(item)
        total += menus[item]

print("---- YOUR CART ----")

for item in cart:
    print(f"{item}: ${menus[item]}")

print(f"Total: ${total}")