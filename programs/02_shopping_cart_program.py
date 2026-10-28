# 5. Exercise 2 Shopping Cart Program  

item = input("Enter the item: ")
price = float(input("Enter the price: "))
qty = int(input("Enter the quantity: "))

total = price * qty

print(f"You buy {qty} {item}. Total: ${total}")