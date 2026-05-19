# Simple Linear Regression

n = int(input("Enter number of data points: "))

x = []
y = []

print("Enter X values:")

for i in range(n):
    x.append(float(input()))

print("Enter Y values:")

for i in range(n):
    y.append(float(input()))

sum_x = 0
sum_y = 0
sum_xy = 0
sum_x2 = 0

for i in range(n):
    sum_x += x[i]
    sum_y += y[i]
    sum_xy += x[i] * y[i]
    sum_x2 += x[i] * x[i]

# Regression Coefficients
b = ((n * sum_xy) - (sum_x * sum_y)) / ((n * sum_x2) - (sum_x * sum_x))

a = (sum_y - b * sum_x) / n

print("\nRegression Equation:")
print("y =", a, "+", b, "*x")