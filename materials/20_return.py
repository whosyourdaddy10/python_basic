# 32. Return = A keyword that returns a value from a function

def add(num1, num2):
    return num1 + num2

# print(add(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return f"{first} {last}"

print(create_name("john", "doe"))