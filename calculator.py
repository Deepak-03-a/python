# python calcultor
import math
operator = input("Enter your operator (+ - * / pow sqrt ")
num1 = float(input("Enter the 1st value: "))

if operator == "sqrt":
    result = math.sqrt(num1)
    print(result)
elif operator == "+":
    num2 = float(input("Enter the 2nd value: "))
    result = num1 + num2
    print(result)
elif operator == "-":
    num2 = float(input("Enter the 2nd value: "))
    result = num1 - num2
    print(result)
elif operator == "*":
    num2 = float(input("Enter the 2nd value: "))
    result = num1 * num2
    print(result)
elif operator == "/":
    num2 = float(input("Enter the 2nd value: "))
    result = num1 / num2
    print(result)
elif operator == "pow":
    num2 = float(input("Enter the 2nd value: "))
    result = pow(num1, num2)
    print(result)
else:
    print(f"{operator} is not a valid operator")


