# 13. Weight Converter

unit = input("Enter the unit (kg or lb): ")

if unit == "kg":
    kg = float(input("Enter the weight in kilograms: "))
    lb = kg * 2.20462
else:
    lb = float(input("Enter the weight in pounds: "))
    kg = lb / 2.20462

print(f"The weight in pounds is {lb}")