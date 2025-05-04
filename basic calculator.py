import math

def basic_calculator():
    """
    Performs basic arithmetic operations with memory functions.

    Args:
        None

    Returns:
        None
    """

    memory = 0

    while True:
        print("Available operators:")
        print("  +  Addition")
        print("  -  Subtraction")
        print("  *  Multiplication")
        print("  /  Division")
        print("  pow  Power")
        print("  sqrt  Square Root")
        print("  MC  Memory Clear")
        print("  MR  Memory Recall")
        print("  M-  Memory Subtract")
        print("  MS  Memory Store")
        print("  C  Clear")
        print("  CE  Clear Entry")
        print("  quit  Exit")

        operator = input("Enter an operator: ")

        if operator == "quit":
            break

        if operator in ["+", "-", "*", "/", "pow"]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
            elif operator == "pow":
                result = math.pow(num1, num2)

            print("Result:", result)

        elif operator == "sqrt":
            num = float(input("Enter a number: "))
            if num >= 0:
                result = math.sqrt(num)
                print("Square root:", result)
            else:
                print("Error: Square root of a negative number is not defined.")

        elif operator == "MC":
            memory = 0
            print("Memory cleared.")
        elif operator == "MR":
            print("Memory recalled:", memory)
        elif operator == "M-":
            memory -= result
            print("Memory subtracted:", memory)
        elif operator == "MS":
            memory = result
            print("Memory stored:", memory)
        elif operator == "C":
            num1 = 0
            num2 = 0
            print("Calculator cleared.")
        elif operator == "CE":
            num2 = 0
            print("Last entry cleared.")
        else:
            print("Invalid operator. Please try again.")

if __name__ == "__main__":
    basic_calculator()