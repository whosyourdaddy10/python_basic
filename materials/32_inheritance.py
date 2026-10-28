# 44. Inheritance = Allow a class to inherit attributes and methods from another class

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f"{self} is walking")

class Cat(Pet):

    def speak():
        print("Meow")

class Dog(Pet):
    def speak():
        print("Woof")

cat = Cat("Neko", 7)
dog = Dog("Kuromi", 4)

Cat.speak()
Dog.speak()
