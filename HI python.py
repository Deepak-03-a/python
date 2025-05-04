import math

a = float(input("Enter the length of side 'a': "))
b = float(input("Enter the leght hof other side of triangle 'b': "))

c = math.sqrt(pow(a,2)+ pow(b, 2))

print(f"The hypotenus of the right angle triangle is: {round(c, 2)} ")
