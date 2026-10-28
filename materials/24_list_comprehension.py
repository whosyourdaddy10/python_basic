# 36. List Comprehension = a way to create a new list based on the values of an existing list

# Formula = EXPRESSION for ITEM in LIST if CONDITION 

numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)

numbers = [1, 2, 3, 4, 5]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)

numbers = [1, 2, 3, 4, 5]
odd_numbers = [x for x in numbers if x % 2 != 0]
print(odd_numbers)