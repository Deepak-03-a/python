# factorial.py
def factorial(n):
# Calculating the factorial of a non-negative interger.
    if n==0:
        return 1  
    else:
        return n * factorial(n-1)
        
num = int(input("Enter a non-negative integer: "))
result = factorial(num)

print(f" The factorial of {num} is {result}")
 
   