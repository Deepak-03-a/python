# Function to perform matrix multiplication
def matrix_multiply(A, B):
    # Get the dimensions of the matrices
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # Check if matrices can be multiplied
    if cols_A != rows_B:
        raise ValueError("Number of columns in A must be equal to the number of rows in B")

    # Create the resultant matrix with zeros
    R = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform the multiplication using nested loops
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                R[i][j] += A[i][k] * B[k][j]

    return R

# Given matrices A and B
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[10, 11],
     [20, 21],
     [30, 31]]

# Perform the matrix multiplication
R = matrix_multiply(A, B)

# Print the resultant matrix
print("Resultant Matrix R:")
for row in R:
    print(row)
