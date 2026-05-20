# Binomial and Normal Distribution

# Binomial Distribution
n = int(input("Enter n: "))
p = float(input("Enter probability p: "))
x = int(input("Enter x: "))

# Factorial Function
def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact *= i

    return fact

# Combination
combination = factorial(n) / (factorial(x) * factorial(n - x))

# Binomial Formula
binomial = combination * (p ** x) * ((1 - p) ** (n - x))

print("\nBinomial Probability =", binomial)

# Normal Distribution
mean = float(input("\nEnter mean: "))
std = float(input("Enter standard deviation: "))
value = float(input("Enter x value: "))

pi = 3.14159
e = 2.71828

power = -(((value - mean) ** 2) / (2 * (std ** 2)))

normal = (1 / (((2 * pi) ** 0.5) * std)) * (e ** power)

print("Normal Distribution Value =", normal)

# Mean is in the center
# Mean = average value
# Symmetrical
# Left side and right side are same shape
# Bell-shaped curve
# Mean = Median = Mode
