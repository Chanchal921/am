# Gaussian Elimination

n = int(input("Enter number of variables: "))

A = []

print("Enter augmented matrix coefficients:")

for i in range(n):
    row = []

    for j in range(n + 1):
        value = float(input(f"Enter value at [{i}][{j}]: "))
        row.append(value)

    A.append(row)

# Forward Elimination
for i in range(n):

    for j in range(i + 1, n):

        ratio = A[j][i] / A[i][i]

        for k in range(n + 1):
            A[j][k] = A[j][k] - ratio * A[i][k]

# Back Substitution
x = [0 for i in range(n)]

x[n - 1] = A[n - 1][n] / A[n - 1][n - 1]

for i in range(n - 2, -1, -1):

    sum_value = 0

    for j in range(i + 1, n):
        sum_value += A[i][j] * x[j]

    x[i] = (A[i][n] - sum_value) / A[i][i]

print("\nSolution:")

for i in range(n):
    print(f"x{i + 1} = {x[i]}")