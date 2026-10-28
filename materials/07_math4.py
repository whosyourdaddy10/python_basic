# 10. Import Math (Find Area)

import math

# 1. Radius of a circle

radius = float(input("Enter the radius: "))

area = math.pi * pow(radius, 2)

print(f"The area of t he circle is {area}")

# 2. Pythagoras Theorem

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The length of side c is {c}")