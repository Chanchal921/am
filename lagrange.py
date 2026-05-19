# Lagrange Interpolation

n = int(input("Enter number of data points: "))

x = []
y = []

print("Enter x values:")

for i in range(n):
    x.append(float(input()))

print("Enter y values:")

for i in range(n):
    y.append(float(input()))

value = float(input("Enter interpolation value: "))

result = 0

for i in range(n):

    term = y[i]

    for j in range(n):

        if i != j:
            term = term * (value - x[j]) / (x[i] - x[j])

    result += term

print("\nInterpolated Value =", result)