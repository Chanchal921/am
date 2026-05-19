# Matrix Addition, Multiplication and Scalar Multiplication

# Input matrix dimensions
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# First Matrix
print("Enter elements of Matrix A:")
A = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"A[{i}][{j}] = "))
        row.append(value)
    A.append(row)

# Second Matrix
print("Enter elements of Matrix B:")
B = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"B[{i}][{j}] = "))
        row.append(value)
    B.append(row)

# Matrix Addition
print("\nMatrix Addition:")
addition = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    addition.append(row)

for row in addition:
    print(row)

# Scalar Multiplication
scalar = int(input("\nEnter scalar value: "))

print("\nScalar Multiplication of Matrix A:")
scalar_matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] * scalar)
    scalar_matrix.append(row)

for row in scalar_matrix:
    print(row)

# Matrix Multiplication
print("\nMatrix Multiplication:")
result = []

for i in range(rows):
    row = []
    for j in range(cols):
        sum_value = 0

        for k in range(cols):
            sum_value += A[i][k] * B[k][j]

        row.append(sum_value)

    result.append(row)

for row in result:
    print(row)