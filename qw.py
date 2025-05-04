def print_heart(n):
    if n % 2 != 0:
        print("Please enter an even integer.")
        return

    half_n = n // 2
    for i in range(half_n):
        if i == 0:
            print(" "*(half_n-i) + "*" + " "*(2*i+1) + "*")
        elif i == half_n - 1:
            print("*" + "ABC" + " "*(2*n-5) + "*")
        else:
            print(" "*(half_n-i) + "*" + " "*(2*i-1) + "ABC" + " "*(2*(half_n-i)-1) + "*")

    for i in range(half_n):
        print(" "*(i+1) + "*" + " "*(2*(half_n-i)-3) + "*")

n = 8
print_heart(n)