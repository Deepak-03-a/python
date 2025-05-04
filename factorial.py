
def fact(n):
    result = 1
    while n >= 1:
        result *= n
        n -= 1
    return result

number = int(input("Enter the number: "))
factorial = fact(number)
print("factorial of " , number, "is" , factorial)