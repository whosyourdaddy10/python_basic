# 33. Arguments = 

# Positional = Arguments that are passed to a function in the same order as they are defined

def say_hello(name, age):
    print(f"Hello, {name}! You are {age} years old.")

say_hello("Rahfi", 28)

# Keyword = Arguments that are passed to a function using the name of the argument

say_hello(age=28, name="Rahfi")

# Default = Arguments that have a default value

def say_hello(name, age=28):
    print(f"Hello, {name}! You are {age} years old.")

say_hello("Rahfi")

# Arbitrary = Arguments that are passed to a function as a tuple

def say_hello(*names):
    for name in names:
        print(f"Hello, {name}!")

say_hello("Rahfi", "John", "Jane")

# *args = Arguments that are passed to a function as a tuple

def say_hello(*names):
    for name in names:
        print(f"Hello, {name}!")

say_hello("Rahfi", "John", "Jane")

# **kwargs = Arguments that are passed to a function as a dictionary

def say_hello(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

say_hello(name="Rahfi", age=28)
