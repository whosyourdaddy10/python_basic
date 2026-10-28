# 45. Multiple dan Multilevel Inheritance

class Animal():
    def __init__(self, name):
        self.name = name

    def eat(self, name):
        print(f"{name} is eating")

class Prey(Animal):
    def flee(self):
        print("This animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    def run(self):
        print("This rabbit is running")

class Hawk(Predator):
    def fly(self):
        print("The hawk is flying")

# Multiple Inheritance = Allow a class to inherit attributes and methods from multiple classes

class Fish(Prey, Predator):

    def swim(self):
        print("The fish is swimming")

fish = Fish("Nemo")
fish.swim()
# Inherit from the Prey class
fish.flee()
# Inherit from the Predator class
fish.hunt()

# Multilevel Inheritance = Allow a class to inherit attributes and methods from another class

class Cat(Predator):
    def speak(self):
        print("Meow")

cat = Cat("Erick")
cat.speak()
cat.hunt()
# Inherit from the Predator class that inherits from the Animal class
cat.eat("Erick")
