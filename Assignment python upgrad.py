def print_heart(n):
    """Prints a heart shape using loops and mathematical formulations.

    Args:
        n: An even integer representing the number of lines in the heart.
    """

    if n % 2 != 0:
        raise ValueError("n must be an even integer.")

    half_n = n // 2
    for i in range(half_n):
        print(" " * (half_n - i), end="")
        print("*" * (2 * i + 1), end=" ")
        print("*" * (2 * i + 1))

    print(" " * half_n, end="")
    print("ABC", end=" ")
    print(" " * half_n)

    for i in range(half_n - 1, -1, -1):
        print(" " * (half_n - i), end="")
        print("*" * (2 * i + 1), end=" ")
        print("*" * (2 * i + 1))

# Get the input from the user
n = int(input("Enter an even integer: "))

# Print the heart
print_heart(n)