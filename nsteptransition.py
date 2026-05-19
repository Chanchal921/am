# Markov Chain n-Step Transition Probability

n = int(input("Enter size of transition matrix: "))

P = []

print("Enter transition matrix:")

for i in range(n):
    row = []

    for j in range(n):
        value = float(input(f"P[{i}][{j}] = "))
        row.append(value)

    P.append(row)

steps = int(input("Enter number of steps: "))

# Copy Matrix
result = []

for i in range(n):
    row = []

    for j in range(n):
        row.append(P[i][j])

    result.append(row)

# Matrix Multiplication Function
def multiply(A, B, n):

    temp = []

    for i in range(n):
        row = []

        for j in range(n):
            sum_value = 0

            for k in range(n):
                sum_value += A[i][k] * B[k][j]

            row.append(sum_value)

        temp.append(row)

    return temp

# Power of Matrix
for s in range(steps - 1):
    result = multiply(result, P, n)

print("\nTransition Matrix after", steps, "steps:")

for row in result:
    print(row)