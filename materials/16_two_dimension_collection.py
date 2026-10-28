# 23. 2D Collection

fruita = ["apple, banana, cherry"]
vegetables = ["carrot, potato, tomato"]
meats = ["beef, chicken, lamb"]

groceries = [fruita, vegetables, meats]

# for grocery in groceries:
#     for item in grocery:
#         print(item)

num_pad = ((1, 2, 3), 
        (4, 5, 6), 
        (7, 8, 9),
        ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()