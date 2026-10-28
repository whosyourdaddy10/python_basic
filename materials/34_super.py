# 46. Super = Function used in a child class 
#             to call a method in the parent class

import math

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"The {self.color} shape is {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

# Overwriting the describe method from the parent class
    def describe(self):
        print(f"It is a circle with an area of {math.pi * pow(self.radius, 2)}cm^2")
# Extending the describe method from the parent class 
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, base, height):
        super().__init__(color, is_filled)
        self.base = base
        self.height = height

circle = Circle(color = "red", is_filled = True, radius = 5)
square = Square(color = "blue", is_filled = False, width = 10)
triangle = Triangle(color = "green", is_filled = True, base = 8, height = 6)

print(circle.color)
print(circle.is_filled)
print(circle.radius)

circle.describe()