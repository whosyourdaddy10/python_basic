# 12. Simple Calculator

operators = input("Enter an operator (+, -, *, /): "    )
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operators == "+":
    result = num1 + num2
    print(round(result, 2))
elif operators == "-":
    result = num1 - num2
    print(round(result, 2))
elif operators == "*":
    result = num1 * num2
    print(round(result, 2))
elif operators == "/":
    result = num1 / num2
    print(round(result, 2))
else:
    print("Invalid operator")