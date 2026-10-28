# 27. Random Number

import random

# print(help(random))

random_number = random.randint(1, 100)
random_float_number = random.random()
options = random.choice(["rock", "paper", "scissors"])
cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

random.shuffle(cards)

print(random_number)
print(random_float_number)
print(options)
print(cards)