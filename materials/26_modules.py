# 38. Modules = A file that contains Python code

# math, random, datetime, sys

import math
# import math as m

pi = math.pi

def circle_area (radius):
    return pi * pow(radius, 2)

print(circle_area(5))

def circumference (radius):
    return 2 * pi * radius

# import circumference in another file (27_modules_two.py)