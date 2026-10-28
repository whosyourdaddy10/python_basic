# 14. Logical Operators (AND, OR, NOT)

# AND: both cconditions must be true
# OR: at least one condition must be true
# NOT: reverse the result

temp = 25
is_raining = True

if temp >= 25 and not is_raining:
    print("It's a hot day")
else:
    print("It's not a hot day")