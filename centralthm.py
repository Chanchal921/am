# Central Limit Theorem Demonstration

n = int(input("Enter sample size: "))

numbers = []

print("Enter sample values:")

for i in range(n):
    value = float(input())
    numbers.append(value)

# Mean Calculation
sum_value = 0

for value in numbers:
    sum_value += value

mean = sum_value / n

# Variance
variance_sum = 0

for value in numbers:
    variance_sum += (value - mean) ** 2

variance = variance_sum / n

# Standard Deviation
std = variance ** 0.5

print("\nMean =", mean)
print("Variance =", variance)
print("Standard Deviation =", std)

print("\nAs sample size increases, sampling distribution approaches normal distribution.")