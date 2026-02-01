# Simple Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation: +, -, *, /")
op = input("Operation: ")

if op == '+':
    print("Result:", num1 + num2)
elif op == '-':
    print("Result:", num1 - num2)
elif op == '*':
    print("Result:", num1 * num2)
elif op == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation").            # Simple Calculator
# Created by a high school student learning Python

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
