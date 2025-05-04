# printing a rectangle with symbols user want to print.

rows = int(input("Enter the number of rows: "))

columns = int(input("Enter number of columns: "))

symbol = input("Enter the symbol which you want to print:  ")

for x in range(rows):
    for y in range(columns):
        print(symbol,end="")
    print()