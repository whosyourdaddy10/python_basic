# 47. Polymorphism = Ability to take different forms

# Inheritance = An Object could be treated of the same type as
#               a parent class

from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * pow(self.radius, 2)

class Square(Shape):
    def __init__(self, width):
        self.width = width

    def area(self):
        return pow(self.width, 2)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
# Considering forms of Pizza, Circle, and Shape
class Pizza(Circle):
    def __init__(self, topping, radius):
        self.topping = topping
        super().__init__(radius)

shapes = [Circle(5), Square(10), Triangle(8, 6), Pizza("pepperoni", 5)]

for shape in shapes:
    print(shape.area())