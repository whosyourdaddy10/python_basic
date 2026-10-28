# 3. Input = A function that prompts the user to enter data and returns it as a string

name = input("Enter your name: ")
age = input("Enter your age: ")

# increase age by 1 to prove that it is a string
age = int(age)
age = age + 1
# or
# age = int(input("Enter your age: "))


print(f"Hello, {name}!") # H
print(f"You are {age} years old.") # Hello, (name)