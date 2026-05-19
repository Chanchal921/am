# t and f Distribution Values

# t Distribution Approximation

sample_mean = float(input("Enter sample mean: "))
pop_mean = float(input("Enter population mean: "))
std = float(input("Enter sample standard deviation: "))
n = int(input("Enter sample size: "))

# t Statistic
t = (sample_mean - pop_mean) / (std / (n ** 0.5))

print("\nt Statistic =", t)

# f Distribution

var1 = float(input("\nEnter first variance: "))
var2 = float(input("Enter second variance: "))

f = var1 / var2

print("f Statistic =", f)