# 43. Object Oriented Programming (OOP) = a programming paradigm that uses 
#     objects and their interactions to model real-world entities

# Class = A template/blueprint for creating objects

class Person:
    # Constructor = A special method that is called when an object is created
    def __init__(self, name, age):  
        self.name = name
        self.age = age
    # Method = A function that belongs to a class
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person = Person("Rahfi", 28)
person.say_hello()

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive (self):
        print(f"The {self.brand} {self.model} is driving.")

    def stop (self):
        print(f"The {self.brand} {self.model} is stopped.")
